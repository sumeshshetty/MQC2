import json
import os
import subprocess
import shlex
import boto3
import itertools
from pymediainfo import MediaInfo
def blackbarDetect(qc_details):
    print("Excecuting blackbarDetect")
    # media_info = MediaInfo.parse(url, library_file='/home/ec2-user/mediaQcApi/MQC2/libs/libmediainfo/libmediainfo.so.0')
    # print(media_info.tracks)
    duration=int([track.to_data()['duration'] for track in qc_details['media_info_data'].tracks][0])/2000 ##Getting half the video duration
    ffmpeg_cmd = f"ffmpeg -ss {duration} -i {qc_details['video_url']} -vframes 100  -vf cropdetect=24:16:0 /tmp/mp4.mp4 -y"  ##checking cropping at mid of the video for 100 frames
    command1 = shlex.split(ffmpeg_cmd)
    print(command1)
    p1 = subprocess.run(command1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p1=p1.stderr
    # print("FFMPEG RESPONSE:",str(p1).encode())
    response=p1.decode().split('\n') 
    crop_list=[]
    crop_list=[item.split('crop=')[1] for item in response  if "crop=" in item]
    cropt_details=crop_list[0].split(':')
    # cropt_details=crop_list[0]
    print("CROP DETAILS:",cropt_details)
    if int(cropt_details[2])>0 or int(cropt_details[3])>0:
        return {"Black Bar Detect":{'X-Offset-Pixels':cropt_details[2],'Y-Offset-Pixels':cropt_details[3]
        ,'Width-Pixels':cropt_details[0],'Height-Pixels':cropt_details[1]}}