from pprint import pprint
from pymediainfo import MediaInfo 

def langDetect(qc_details):
	print("Excecuting langDetect")
	# media_info = MediaInfo.parse(url, library_file='/home/ec2-user/mediaQcApi/MQC2/libs/libmediainfo/libmediainfo.so.0')
	language="No Audio Found"
	for track in qc_details['media_info_data'].tracks:
		if track.track_type == "Audio":
			media_info=track.to_data()
			# print(media_info)
			try:
				language = media_info['language']
				print(f"Language:", language)
				return {"Audio Language":language}
			except KeyError:
				# language ="Exception: Not able to detect language" 
				pass

	