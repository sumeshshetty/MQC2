from moviepy.editor import *
import cv2
import numpy as np
from time import sleep
from collections import namedtuple

#filename = 'C:/users/yahyasirguroh/downloads/96p_mp4.mp4'

def BrightnessDetect(url):
	BLevel = namedtuple("BLevel", ['brange', 'bval'])
	_blevels = [
	BLevel(brange=range(0, 24), bval=0),
    BLevel(brange=range(23, 46), bval=1),
    BLevel(brange=range(47, 69), bval=2),
    BLevel(brange=range(70, 93), bval=3),
    BLevel(brange=range(92, 115), bval=4),
    BLevel(brange=range(116, 139), bval=5),
    BLevel(brange=range(140, 162), bval=6),
    BLevel(brange=range(163, 185), bval=7),
    BLevel(brange=range(186, 208), bval=8),
    BLevel(brange=range(209, 231), bval=9),
    BLevel(brange=range(232, 256), bval=10)
    ]
    video = VideoFileClip(url)
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
    Message="video brightness : %g (values ranges from 0 to 10)" % detect_brightness

    if detect_brightness<=2:
    	print("Brightness level is between 0 to 69")
    	Message="Brightness level is between 0 to 69"
    	print("video is very low brightness level")
    	Message="video is very low brightness level"
    elif detect_brightness<=6:
    	if detect_brightness==3:
    		print("Brightness level is between 70 to 92")
    		Message="Brightness level is between 70 to 92"
    		print("Video is Fair Brightness level")
    		Message="Video is Fair Brightness level"
    	elif detect_brightness==4:
    		print("Brightness level is between 93 to 115")
    		Message="Brightness level is between 93 to 115"
    		print("Video is Good Brightness level")
    		Message="Video is Good Brightness level"
    	elif detect_brightness==5:
    		print("Brightness level is between 116 to 139")
    		Message="Brightness level is between 116 to 139"
    		print("Video is Very Good Brightness level")
    		Message="Video is Very Good Brightness level"
    	elif detect_brightness==6:
    		print("Brightness level is between 140 to 162")
    		Message="Brightness level is between 140 to 162"
    		print("Video is Excellent Brightness level")
    		Message="Video is Excellent Brightness level"
    else:
    	if detect_brightness==7:
    		print("Brightness level is between 163 to 185")
    		Message="Brightness level is between 163 to 185"
    	elif detect_brightness==8:
    		print("Brightness level is between 186 to 208")
    		Message="Brightness level is between 186 to 208"
    	elif detect_brightness==9:
    		print("Brightness level is between 209 to 231")
    		Message="Brightness level is between 209 to 231"
    	elif detect_brightness==10:
    		print("Brightness level is between 232 to 256")
    		Message="Brightness level is between 232 to 256"
    	print("Video Brightness level is very High Effective For Human Eyes")
    	Message="Video Brightness level is very High Effective For Human Eyes"













