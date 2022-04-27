import moviepy.editor
import os

def audioLevel(qc_details):
	try:
		print("Excecuting audioLevel")
		# video = moviepy.editor.VideoFileClip(url)
		
		# audio = video.audio
		if  not qc_details['audio_url']:
			print("No audio")
			return {"Audio Levels":"No Audio file Detected"}
		# file_path='tmp/temp.wav'
		# audio.write_audiofile(file_path)
		audio_segment = AudioSegment.from_file(qc_details['audio_url'])
		dBFS=audio_segment.dBFS
		print(f"Intensity-dBFS : {dBFS}")


		# between -15 and -6 dBFS good
		#<-15 bad

		if -15<dBFS<-6:
			print("good audio")
			message="Good Audio Level"
		if dBFS<-15:
			print("bad audio")
			message="Bad Audio Level"


		# os.remove("tmp/temp.wav")
		audio_dict={
		"Audio Decibels":dBFS,
		"message":message
		}
		
	except Exception as err:
		print(f"Error in audioLevel : {err}")
		audio_dict="Exception: No Audiolevel Detected"
	print(f"audioLevel audio_dict: {audio_dict}")	
	return {"Audio Levels":audio_dict}


