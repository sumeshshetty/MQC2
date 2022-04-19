from datetime import timedelta
import cv2
import numpy as np
import os
from PIL import Image as im
import imagehash
import subprocess ,shlex
import time

def DuplicateFrame(url):
	try:
		cap = cv2.VideoCapture(url)
		fps = cap.get(cv2.CAP_PROP_FPS)
		fps=cap.set(cv2.CAP_PROP_POS_MSEC,7000)
		read,frame=cap.read()
		count=1
		value=[]
		fra=[]
		fp1=[]
		while read:
			cap.set(cv2.CAP_PROP_POS_MSEC,count*1000)
			read,frame=cap.read()
			if read:
				ti=cap.get(cv2.CAP_PROP_POS_MSEC)
				seconds=(ti/1000)%60
				minutes=(ti/(1000*60))%60
				hours=(ti/(1000*60*60))%24
				im2 = im.fromarray(frame)
				has2=imagehash.average_hash(im2)
				has2=str(has2)
				if has2 not in value:
					value.append(has2)
					frame_time=round(hours, 4) ,round(minutes, 4),round(seconds, 4)
				else:
					time_1=(round(hours, 4) ,round(minutes, 4), round(seconds, 4))
					print(f"This Duplicate frame is exist {has2}  on time is {frame_time} to {time_1}")
				fra.append(frame)
				count+=1
		Duplicate_Frames={
		"HashValue":has2,
		"From":frame_time,
		"To":time_1
		}
	except Exception as err:
		print(f"Error in DuplicateFrame : {err}")
		Duplicate_Frames="Exception: No DuplicateFrame Detected"

	print(f"Duplicate Frame: {Duplicate_Frames}")
	return{"Duplicate Frame":Duplicate_Frames}