

from scipy import arange
import moviepy.editor
import soundfile
import numpy,scipy,scipy.fftpack
import os

def audioLevel(url):
	try:
		print("Excecuting audioLevel")
		video = moviepy.editor.VideoFileClip(url)
		
		audio = video.audio
		if  not audio:
			print("No audio")
			return {"Audio data":"no audio file"}
		audio.write_audiofile("tmp/temp.wav")

		file_path='tmp/temp.wav'


		audio_samples,sample_rate=soundfile.read(file_path,dtype='int16')
		number_samples=len(audio_samples)
		print('Audio samples ',audio_samples)
		print('Number of Sample',number_samples)
		print('Frequency is : ',sample_rate,'HZ')
		if sample_rate<=5000:
			print("Minimum Sound Level",sample_rate)
			message=f"Minimum Sound Level: {sample_rate}"

		duration=round(number_samples/sample_rate,2)
		print('Audio Duration: {0}s'.format(duration))
		if sample_rate>25000:
			print("Maximum Sound Level",sample_rate)
			message=f"Maximum Sound Level: {sample_rate}"


		freq_bins=numpy.arange(number_samples) * sample_rate/number_samples
		if sample_rate>5000 and  sample_rate<20000:
			print("Average Sound Level",sample_rate)
			message=f"Average Sound Level: {sample_rate}"

		os.remove("tmp/temp.wav")
		audio_dict={
		"Frequency":sample_rate,
		"message":message
		}
		
	except Exception as err:
		print(f"Error in audioLevel : {err}")
		audio_dict="Exception: No Audiolevel Detected"
	print(f"audioLevel audio_dict: {audio_dict}")	
	return {"Audio Levels":audio_dict}


