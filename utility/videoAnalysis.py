
from utility.checks.video.logoDetect import logoDetect
from utility.checks.video.lightLevelDetect import lightLevelDetect
from utility.checks.video.freezeFrame import freezeFrame
from utility.checks.video.blackFrame import blackFrame
def videoAnalysis(url):

	#logoDetectjson=logoDetect()
	#lightLevelDetectjson=lightLevelDetect(url)
	freezeFramejson=freezeFrame(url)
	blackFramejson=blackFrame(url)

	video_report=[]
	#video_report.append(lightLevelDetectjson)
	video_report.append(freezeFramejson)
	video_report.append(blackFramejson)
	return video_report
