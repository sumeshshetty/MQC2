from datetime import timedelta
import cv2
import numpy as np
import time
import moviepy.editor
from scipy.io import wavfile
from scipy.fft import *

def HighFrequencyNoise(qc_details):
	url=qc_details['video_url']
	cap = cv2.VideoCapture(url)
	fps = cap.get(cv2.CAP_PROP_FPS)
	fps=cap.set(cv2.CAP_PROP_POS_MSEC,7000)
	read,frame=cap.read()
	count=1
	while read:
		cap.set(cv2.CAP_PROP_POS_MSEC,count*1000)
		read,frame=cap.read()
		if read:
			ti=cap.get(cv2.CAP_PROP_POS_MSEC)
			milisecond=((ti/1000)%60)*1000
			frame_time=round((milisecond/1000)%60, 4)
			file=qc_details['audio_url']
			sr, data = wavfile.read(file)
			if data.ndim > 1:
				data = data[:, 0]
			else:
				pass
			dataToRead = data[int(milisecond * sr / 1000) : int(2*milisecond * sr / 1000) + 1]
			N = len(dataToRead)
			yf = rfft(dataToRead)
			xf = rfftfreq(N, 1 / sr)
			idx = np.argmax(np.abs(yf))
			freq = xf[idx]
			if freq>=2000:
				print(f"High Frequency Noise at:{frame_time} sec with {int(freq)}Hz")
				return {"High Frequency Noise":str(freq)+" Hz",
				       "TimeStamp":str(frame_time)+" sec"
				       }
			else:
				pass
			count+=1	





