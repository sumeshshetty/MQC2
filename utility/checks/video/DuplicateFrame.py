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
					start_time=round(seconds, 4)
				else:
					end_time=round(seconds, 4)
					print(f"This Duplicate frame is exist {has2}  on time is {start_time} to {end_time}")
					#in sec
					# Create a list of all values in list of dictionaries
					# list_of_all_values = [elem.get('start') for elem in Duplicate_Frames]
					# print(list_of_all_values)
					# if start_time not in list_of_all_values:
					
					dict_obj={"start":start_time,"end":end_time}
					Duplicate_Frames.append(dict_obj.copy())

				fra.append(frame)
				count+=1
		
	except Exception as err:
		print(f"Error in DuplicateFrame : {err}")
		Duplicate_Frames="Exception: No DuplicateFrame Detected"

	print(f"Duplicate Frame:\n {Duplicate_Frames}")
	return{"Duplicate Frame":Duplicate_Frames}