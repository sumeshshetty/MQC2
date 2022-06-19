import cv2
import numpy as np
from collections import namedtuple

def contrastDetect(qc_details):
	url=qc_details['video_url']
	img = cv2.VideoCapture(url)

	ret, frame = img.read()
	Y = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)[:,:,0]
	min = np.min(Y)
	max = np.max(Y)
	contrast = (max-min)/(max+min)
	print("contrast:",contrast)
	

	if contrast<1.0:
	    print("video is very low contrast level")
	    Message="Bad contrast level"

	if contrast>=1.0:
	    print("Video is Good contrast level")
	    Message="Good contrast level"
	# else:
	#     print("Video contrast level is very High Effective For Human Eyes")
	#     Message="Bad contrast level" 
	return {"Contrast Detect":Message}



