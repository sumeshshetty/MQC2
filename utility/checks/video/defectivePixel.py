import cv2 
import os
import time
from PIL import Image  

def defectivePixel(qc_details):
	try:
		print("Excecuting defectivePixel")
		white = 0
		gray = 0
		black = 0
		red= 0



		frame1=[]
		currentframe = []
		currentframe.append(0)
		count=1

		pixel_list = []

		cap = cv2.VideoCapture(qc_details['video_url']) 
		while(True): 
			ret,frame = cap.read()
			cap.set(cv2.CAP_PROP_POS_MSEC,count*1000)
			read,frame=cap.read() 
			if read:
				ti=cap.get(cv2.CAP_PROP_POS_MSEC)
				
				seconds=(ti/1000)
				minutes=(ti/(1000*60))%60
				hours=(ti/(1000*60*60))%24

				
			if ret: 
				name = 'frame' + str(currentframe[-1])
				currentframe.append((currentframe[-1]+1))
				frame1.append(frame)
				count+=1
				for i in frame1:
					im1=i
					try:
						im1=Image.fromarray(im1)
						

						for pixel in im1.getdata():
							if pixel == (255, 255, 255): 
								white += 1
							if pixel==(0,0,0):  
								black+=1
							if pixel==(139,0,0):   
								red+=1
					except Exception as e:
						print("Error in defectivePixel:",e)
						pixel_list.append({"Error message":str(e)})
						print("pixel_list:",pixel_list)
						return {"Defective Pixel":pixel_list}
						

				time.sleep(0)
				
				
				print('Stuck Pixel=' + str(white)+', Dead Pixel='+str(black)+',  Hot Pixel='+str(red))

				# print(round(hours, 4) ,":",round(minutes, 4),":",round(seconds, 4))
				# timestamp=str(round(hours, 2))+":"+str(round(minutes, 2))+":"+str(round(seconds, 2)) #changed from 4-->2 decimals
				timestamp=round(seconds, 2)
				pixel_dict={
				"timestamp":timestamp,
				"Stuck Pixel":white,
				"Dead Pixel":black,
				"Hot Pixel":red
				}
				pixel_list.append(pixel_dict)
				if len(currentframe)==10:
					break
					
		# cap.release()
		# cv2.destroyAllWindows()
	except Exception as err:
		print(f"Error in defectivePixel : {err}")
		pixel_list="No Defective Pixel Detected"
	print(f"Defective Pixel: {pixel_list}")

	return {"Defective Pixel":pixel_list}
