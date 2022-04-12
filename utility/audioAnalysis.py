
from utility.checks.audio.langDetect import langDetect
def audioAnalysis(url):
	langDetectjson=langDetect(url)

	audio_report=[]
	audio_report.append(langDetectjson)
	return audio_report