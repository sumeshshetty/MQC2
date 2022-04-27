import moviepy.editor
def create_audio_file(qc_details):
	print("Excecuting create_audio_file")
	video = moviepy.editor.VideoFileClip(qc_details['video_url'])
	
	audio = video.audio
	if  audio:
		qc_details['audio_url']=f'{qc_details['video_url'].rsplit('.')[-2]}.wav'
		audio.write_audiofile(qc_details['audio_url'])
	else:
		print("No Audio file")
		qc_details['audio_url']=""

	return qc_details