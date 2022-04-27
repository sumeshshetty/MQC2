from utility.checks.video.lightLevelDetect import lightLevelDetect
from utility.checks.video.freezeFrame import freezeFrame
from utility.checks.video.blackFrame import blackFrame
from utility.checks.video.defectivePixel import defectivePixel
from utility.checks.video.DuplicateFrame import DuplicateFrame
from utility.checks.video.BrightnessDetect import BrightnessDetect
from utility.checks.video.blackbarDetect import blackbarDetect
def videoAnalysis(qc_details):

	#logoDetectjson=logoDetect()
	lightLevelDetectjson=lightLevelDetect(qc_details)
	freezeFramejson=freezeFrame(qc_details)
	blackFramejson=blackFrame(qc_details)
	defectivePixeljson=defectivePixel(qc_details)
	# DuplicateFramejson=DuplicateFrame(qc_details)
	BrightnessDetectjson=BrightnessDetect(qc_details)
	blackbarDetectjson=blackbarDetect(qc_details)

	video_report=[]
	video_report.append(lightLevelDetectjson)
	video_report.append(freezeFramejson)
	video_report.append(blackFramejson)
	video_report.append(defectivePixeljson)
	# video_report.append(DuplicateFramejson)
	video_report.append(BrightnessDetectjson)
	video_report.append(blackbarDetectjson)
	video_report = list(filter(None, video_report))

	return video_report
