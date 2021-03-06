from moviepy.editor import *
import cv2
import numpy as np
from time import sleep
from collections import namedtuple

def BrightnessDetect(qc_details):
    print("Excecuting BrightnessDetect")
    BLevel = namedtuple("BLevel", ['brange', 'bval'])
    _blevels = [
        BLevel(brange=range(0,40), bval=0),
        BLevel(brange=range(40,80), bval=1),
        BLevel(brange=range(80,120), bval=2),
        BLevel(brange=range(120,160), bval=3),
        BLevel(brange=range(160,200), bval=4),
        BLevel(brange=range(200,255), bval=5)
        ]
    video = VideoFileClip(qc_details['video_url'])
    duration = video.duration
    step = 5
    all_frame_b_values= []
    for t in range(int(duration*step)):
        t = t/step
        if  t > video.duration:
            break
        video_frame = video.get_frame(t)
        video_frame = cv2.cvtColor(video_frame, cv2.COLOR_BGR2RGB)
        video_frame = cv2.resize(video_frame,(512,288))
        hsv = cv2.cvtColor(video_frame, cv2.COLOR_RGB2HSV)
        v = hsv[:,:,2]
        m_val = int(v.mean())
        for blevel in _blevels:
            if m_val in blevel.brange:
                brightness = blevel.bval
                all_frame_b_values.append(brightness)
    all_frame_b_values = np.array(all_frame_b_values)
    video_brigtness= (all_frame_b_values.mean())
    detect_brightness=int(video_brigtness)
    print ('video brightness : %g (values ranges from 0 to 10)' %(detect_brightness))
    #Message="video brightness : %g (values ranges from 0 to 10)" %(detect_brightness)

    if detect_brightness==0:
        print("video is very low brightness level")
        Message="Bad Brightness level"
    if detect_brightness<=3:
        print("Video is Good Brightness level")
        Message="Good Brightness level"
    else:
        print("Video Brightness level is very High Effective For Human Eyes")
        Message="Bad Brightness level"

    return{"Video Brightness Level":detect_brightness , "Message":Message}