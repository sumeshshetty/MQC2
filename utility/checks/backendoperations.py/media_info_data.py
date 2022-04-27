from pymediainfo import MediaInfo
def media_info_data(qc_details):
	print("Excecuting media_info_data")
	qc_details['media_info_data'] = MediaInfo.parse(qc_details['video_url'], library_file='/home/ec2-user/mediaQcApi/MQC2/libs/libmediainfo/libmediainfo.so.0')
	return qc_details