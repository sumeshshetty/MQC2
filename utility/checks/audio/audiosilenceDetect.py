from pydub import AudioSegment, silence

def audiosilenceDetect(url):
	print("Excecuting audiosilenceDetect")
	myaudio = intro = AudioSegment.from_file(url)
	dBFS=myaudio.dBFS
	try:
		silence1 = silence.detect_silence(myaudio, min_silence_len=1000, silence_thresh=dBFS-16)
		silence1 = [{"start":start/1000,"end":stop/1000} for start,stop in silence1] #in sec
	except Exception as e:
		print("Error in audiosilenceDetect:",e)
		silence1="Exception: Cannot detect Audio Silence"
	print(f"audiosilenceDetect : {silence1}")
	return {'Audio Silence Detect': silence1}

