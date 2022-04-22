
from utility.checks.audio.langDetect import langDetect
from utility.checks.audio.audiosilenceDetect import audiosilenceDetect
from utility.checks.audio.bitdepthDetect import bitdepthDetect
from utility.checks.audio.audioLevel import audioLevel
def audioAnalysis(url):
	langDetectjson=langDetect(url)
	audiosilenceDetectjson=audiosilenceDetect(url)

	bitdepthDetectjson=bitdepthDetect(url)
	audioLeveljson=audioLevel(url)



	audio_report=[]
	audio_report.append(langDetectjson)
	audio_report.append(audiosilenceDetectjson)

	audio_report.append(bitdepthDetectjson)
	audio_report.append(audioLeveljson)
	audio_report = list(filter(None, audio_report))

	return audio_report