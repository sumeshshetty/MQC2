from pprint import pprint
from pymediainfo import MediaInfo 
def bitdepthDetect(url):
	media_info = MediaInfo.parse(url)
	final_list=[]
	for track in media_info.tracks:
		if track.track_type == "Audio":
			try:
				media_info=track.to_data()
				# print(media_info)
				bit_depth = media_info["bit_depth"]
				print(f"bit_depth:", bit_depth)
				if media_info['bit_depth'] == 16:
					print("Good & Clear Audio")
					Message="Good & Clear Audio"
				elif media_info['bit_depth'] == 24:
					print("Smooth Audio")
					Message="Smooth Audio"
				elif media_info['bit_depth'] == 32: 
					print("Very Smooth Audio")
					Message="Very Smooth Audio"
				else:
					Message="BitDepth is faulty, Audio BitDepth range is 16,24 and 32 for Smooth Audio voice."
					print("BitDepth is faulty, Audio BitDepth range is 16,24 and 32 for Smooth Audio voice.")
			except Exception as err:
				print("Error in bit_depth",err)
				bit_depth="Null"
				Message="Null"
			dict_obj={'Audio_BitDepth' : bit_depth, 'Message' : Message}
			final_list.append(dict_obj)
	return final_list