
from utility.checks.audio.langDetect import langDetect
from utility.checks.audio.audiosilenceDetect import audiosilenceDetect
def audioAnalysis(url):
	langDetectjson=langDetect(url)
	#audiosilenceDetectjson=audiosilenceDetect(url)

	audio_report=[]
	audio_report.append(langDetectjson)
	#audio_report.append(audiosilenceDetectjson)
	return audio_report