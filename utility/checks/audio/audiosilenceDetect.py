from pydub import AudioSegment, silence

def audiosilenceDetect(url):
	myaudio = intro = AudioSegment.from_file(url)
	dBFS=myaudio.dBFS
	try:
		silence1 = silence.detect_silence(myaudio, min_silence_len=1000, silence_thresh=dBFS-16)
		silence1 = [((start/1000),(stop/1000)) for start,stop in silence] #in sec
	except Exception as e:
		print("Error:",e)
		silence1="Cannot detect silence check logs"
	print(silence1)
	return {'Audio Silence Detect': silence1}

