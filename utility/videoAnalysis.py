
from utility.checks.video.logoDetect import logoDetect
from utility.checks.video.lightLevelDetect import lightLevelDetect
def videoAnalysis(url):

	#logoDetectjson=logoDetect()
	lightLevelDetectjson=lightLevelDetect(url)

	video_report=[]
	video_report.append(lightLevelDetectjson)
	return video_report
