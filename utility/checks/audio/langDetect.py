from pprint import pprint
from pymediainfo import MediaInfo 

def langDetect(url):
	media_info = MediaInfo.parse(url)
	for track in media_info.tracks:
		if track.track_type == "Audio":
			media_info=track.to_data()
			print(media_info)
			language = media_info['language']
			print(f"Language:", language)
			return {"Audio Language Detected":language}


















