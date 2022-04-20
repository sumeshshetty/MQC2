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
		print("Excecuting DuplicateFrame")
		cap = cv2.VideoCapture(url)
		fps = cap.get(cv2.CAP_PROP_FPS)
		fps=cap.set(cv2.CAP_PROP_POS_MSEC,7000)
		read,frame=cap.read()
		count=1
		value=[]
		fra=[]
		Duplicate_Frames=[]
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
					Duplicate_Frames.append("This Duplicate frame exist on time is" +str(frame_time)+ "to" +str(time_1))
					frame_duplicate="\n".join(Duplicate_Frames)

				fra.append(frame)
				count+=1
		
	except Exception as err:
		print(f"Error in DuplicateFrame : {err}")
		Duplicate_Frames="Exception: No DuplicateFrame Detected"

	print(f"Duplicate Frame:\n {frame_duplicate}")
	return{"Duplicate Frame":frame_duplicate}