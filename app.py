#install pm2 first
#pm2 start pm2/pm2_config.json
from flask import Flask,request
import json,os
import datetime
import pytz
import logging
from flask_cors import CORS
from utility.audioAnalysis import audioAnalysis
from utility.videoAnalysis import videoAnalysis
from utility.download_s3_object import download_s3_object

#test git bracnh ----newly added today---new form scifi1123 !@###!!
app = Flask(__name__)
CORS(app)

logger = logging.getLogger()

# Configure logger
logging.basicConfig(filename="logs/common-1.log", filemode='a',format='%(asctime)s %(message)s')


# Setting threshold level
logger.setLevel(logging.DEBUG)



@app.route('/api/v1/mediaqc/report',methods=['GET'])
def getQcReport():

	data = request.get_json()

	print("*****data ******")
	print(data)
	print("*****data ******")


	url=data['url']
	local_video_url=download_s3_object(url)
	videoJson=videoAnalysis(local_video_url)
	audioJson=audioAnalysis(local_video_url)
	os.remove(local_video_url)
	final_report=[]

	final_report.append({"Audio Report":audioJson,"Video Report":videoJson})
	print(f"final_report: {final_report}")
	return {"QC report":final_report}


if __name__ == '__main__':
    app.run(port='5001',host="0.0.0.0",debug=True)

