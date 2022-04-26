
from utility.checks.video.logoDetect import logoDetect
from utility.checks.video.lightLevelDetect import lightLevelDetect
from utility.checks.video.freezeFrame import freezeFrame
from utility.checks.video.blackFrame import blackFrame
from utility.checks.video.defectivePixel import defectivePixel
from utility.checks.video.DuplicateFrame import DuplicateFrame
from utility.checks.video.BrightnessDetect import BrightnessDetect
from utility.checks.video.blackbarDetect import blackbarDetect
def videoAnalysis(url):

	#logoDetectjson=logoDetect()
	lightLevelDetectjson=lightLevelDetect(url)
	freezeFramejson=freezeFrame(url)
	blackFramejson=blackFrame(url)
	defectivePixeljson=defectivePixel(url)
	DuplicateFramejson=DuplicateFrame(url)
	BrightnessDetectjson=BrightnessDetect(url)
	blackbarDetectjson=blackbarDetect(url)

	video_report=[]
	video_report.append(lightLevelDetectjson)
	video_report.append(freezeFramejson)
	video_report.append(blackFramejson)
	video_report.append(defectivePixeljson)
	video_report.append(DuplicateFramejson)
	video_report.append(BrightnessDetectjson)
	video_report.append(blackbarDetectjson)
	video_report = list(filter(None, video_report))

	return video_report
