from pprint import pprint
from pymediainfo import MediaInfo

def lightLevelDetect(url):
	media_info = MediaInfo.parse(url)
	for track in media_info.tracks:
		if track.track_type == 'Video':
			media_info=track.to_data()
			#pprint(media_info)
			try:
				MaxCLL = media_info['maximum_content_light_level']
				print(f"MaxCLL:", MaxCLL)
				MaxFALL = media_info['maximum_frameaverage_light_level']
				print(f"MaxFALL:", MaxFALL)
			except KeyError:
				print("Not an HDR10 Video else MaxCLL and MaxFALL check Defective")
	
	return {'MaxCLL Detected' : MaxCLL,
			'MaxFALL Detected' : MaxFALL}