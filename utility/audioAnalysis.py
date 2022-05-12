
from utility.checks.audio.langDetect import langDetect
from utility.checks.audio.audiosilenceDetect import audiosilenceDetect
from utility.checks.audio.bitdepthDetect import bitdepthDetect
from utility.checks.audio.audioLevel import audioLevel
from utility.checks.audio.HighFrequencyNoise import HighFrequencyNoise
def audioAnalysis(qc_details):
	langDetectjson=langDetect(qc_details)
	audiosilenceDetectjson=audiosilenceDetect(qc_details)

	bitdepthDetectjson=bitdepthDetect(qc_details)
	audioLeveljson=audioLevel(qc_details)

	HighFrequencyNoisejson=HighFrequencyNoise(qc_details)



	audio_report=[]
	audio_report.append(langDetectjson)
	audio_report.append(audiosilenceDetectjson)

	audio_report.append(bitdepthDetectjson)
	audio_report.append(audioLeveljson)

	audio_report.append(HighFrequencyNoisejson)
	audio_report = list(filter(None, audio_report))

	return audio_report