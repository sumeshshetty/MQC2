
from utility.checks.audio.langDetect import langDetect
from utility.checks.audio.audiosilenceDetect import audiosilenceDetect
from utility.checks.audio.bitdepthDetect import bitdepthDetect
def audioAnalysis(url):
	langDetectjson=langDetect(url)
	audiosilenceDetectjson=audiosilenceDetect(url)

	bitdepthDetectjson=bitdepthDetect(url)


	audio_report=[]
	audio_report.append(langDetectjson)
	audio_report.append(audiosilenceDetectjson)

	audio_report.append(bitdepthDetectjson)

	return audio_report