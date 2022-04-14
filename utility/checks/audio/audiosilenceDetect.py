from pydub import AudioSegment, silence

def audiosilenceDetect(url):
	myaudio = intro = AudioSegment.from_file(url)
	dBFS=myaudio.dBFS
	silence = silence.detect_silence(myaudio, min_silence_len=1000, silence_thresh=dBFS-16)
	silence = [((start/1000),(stop/1000)) for start,stop in silence] #in sec
	print(silence)
	return {'Audio Silence Detect': silence}

