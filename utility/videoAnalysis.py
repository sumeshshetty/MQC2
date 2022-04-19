
from utility.checks.video.logoDetect import logoDetect
from utility.checks.video.lightLevelDetect import lightLevelDetect
from utility.checks.video.freezeFrame import freezeFrame
from utility.checks.video.blackFrame import blackFrame
from utility.checks.video.defectivePixel import defectivePixel
from utility.checks.video.DuplicateFrame import DuplicateFrame
def videoAnalysis(url):

	#logoDetectjson=logoDetect()
	lightLevelDetectjson=lightLevelDetect(url)
	freezeFramejson=freezeFrame(url)
	blackFramejson=blackFrame(url)
	defectivePixeljson=defectivePixel(url)
	DuplicateFramejson=DuplicateFrame(url)

	video_report=[]
	video_report.append(lightLevelDetectjson)
	video_report.append(freezeFramejson)
	video_report.append(blackFramejson)
	video_report.append(defectivePixeljson)
	video_report.append(DuplicateFramejson)

	return video_report
