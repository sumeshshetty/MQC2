from pymediainfo import MediaInfo
def media_info_data(qc_details):
	print("Excecuting media_info_data")
	qc_details['media_info_data'] = MediaInfo.parse(qc_details['video_url'])
	return qc_details