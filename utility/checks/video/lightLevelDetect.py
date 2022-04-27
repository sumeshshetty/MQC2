from pprint import pprint
from pymediainfo import MediaInfo

def lightLevelDetect(qc_details):
	print("Excecuting lightLevelDetect")
	# media_info = MediaInfo.parse(url, library_file='/home/ec2-user/mediaQcApi/MQC2/libs/libmediainfo/libmediainfo.so.0')
	
	for track in qc_details['media_info_data'].tracks:
		if track.track_type == 'Video':
			media_info=track.to_data()
			
			try:
				MaxCLL = media_info['maximum_content_light_level']
				print(f"MaxCLL:", MaxCLL)
				MaxFALL = media_info['maximum_frameaverage_light_level']
				print(f"MaxFALL:", MaxFALL)
			except KeyError:
				MaxCLL=''
				MaxFALL=''
				print("Not an HDR10 Video else MaxCLL and MaxFALL check Defective")
	if MaxCLL:
		response={'MaxCLL Detected' : MaxCLL,'MaxFALL Detected' : MaxFALL}
		return response