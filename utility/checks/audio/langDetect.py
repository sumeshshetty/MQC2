from pprint import pprint
from pymediainfo import MediaInfo 

def langDetect(url):
	print("Excecuting langDetect")
	media_info = MediaInfo.parse(url, library_file='/home/ec2-user/mediaQcApi/MQC2/libs/libmediainfo/libmediainfo.so.0')
	language="No Audio Found"
	for track in media_info.tracks:
		if track.track_type == "Audio":
			media_info=track.to_data()
			# print(media_info)
			try:
				language = media_info['language']
			except KeyError:
				language ="Exception: Not able to detect language"
	
	print(f"Language:", language)

	return {"Audio Language":language}