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
from utility.backendoperations.download_s3_object import download_s3_object
from utility.backendoperations.media_info_data import media_info_data
from utility.backendoperations.create_audio_file import create_audio_file

#test git bracnh ----newly added today---new form scifi1123 !@###!!
app = Flask(__name__)
CORS(app)

logger = logging.getLogger()

# Configure logger
logging.basicConfig(filename="logs/common-1.log", filemode='a',format='%(asctime)s %(message)s')


# Setting threshold level
# logger.setLevel(logging.DEBUG)



@app.route('/api/v1/mediaqc/report',methods=['GET'])
def getQcReport():
	qc_details={}
	data = request.get_json()

	print("*****data ******")
	print(data)
	print("*****data ******")


	url=data['url']
	local_video_url,status=download_s3_object(url)
	if status=="Downloaded":
		qc_details['video_url']=local_video_url

		qc_details=media_info_data(qc_details)
		qc_details=create_audio_file(qc_details)

		videoJson=videoAnalysis(qc_details)
		audioJson=audioAnalysis(qc_details)
		os.remove(qc_details['video_url'])
		if qc_details['audio_url']:
			os.remove(qc_details['audio_url'])
		final_report=[]

		final_report.append({"Audio Report":audioJson,"Video Report":videoJson})
	else:
		final_report="Please Check the S3 path provided"


	print(f"final_report: {final_report}")
	return {"QC report":final_report}


if __name__ == '__main__':
    app.run(port='5001',host="0.0.0.0",debug=True)

