
from utility.checks.video.logoDetect import logoDetect
from utility.checks.video.lightLevelDetect import lightLevelDetect
from utility.checks.video.freezeFrame import freezeFrame
def videoAnalysis(url):

	#logoDetectjson=logoDetect()
	#lightLevelDetectjson=lightLevelDetect(url)
	freezeFramejson=freezeFrame(url)

	video_report=[]
	#video_report.append(lightLevelDetectjson)
	video_report.append(freezeFramejson)
	return video_report
