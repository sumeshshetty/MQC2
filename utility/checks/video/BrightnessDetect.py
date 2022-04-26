from moviepy.editor import *
import cv2
import numpy as np
from time import sleep
from collections import namedtuple

def BrightnessDetect(url):
	BLevel = namedtuple("BLevel", ['brange', 'bval'])
	_blevels = [
        BLevel(brange=range(0,51), bval=0),
        BLevel(brange=range(51,102), bval=1),
        BLevel(brange=range(102,153), bval=2),
        BLevel(brange=range(153,204), bval=3),
        BLevel(brange=range(204,255), bval=4),
        
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
    #Message="video brightness : %g (values ranges from 0 to 10)" %(detect_brightness)

    if detect_brightness<=1:
    	print("video is very low brightness level")
    	Message="video is very low brightness level"
    elif detect_brightness==2:
        print("Video is Good Brightness level")
        Message="Video is Good Brightness level"
    else:
        print("Video Brightness level is very High Effective For Human Eyes")
    	Message="Video Brightness level is very High Effective For Human Eyes"

    return{"Video Brightness":Message}    

    	













