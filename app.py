#install pm2 first
#pm2 start pm2/pm2_config.json
from flask import Flask,request
import json
import datetime
import pytz
import logging
from flask_cors import CORS
from utility.audioAnalysis import audioAnalysis
from utility.videoAnalysis import videoAnalysis

#test git bracnh ----newly added today---new form scifi1123
app = Flask(__name__)
CORS(app)

logger = logging.getLogger()

# Configure logger
logging.basicConfig(filename="logs/common-1.log", filemode='a',format='%(asctime)s %(message)s')


# Setting threshold level
logger.setLevel(logging.DEBUG)



@app.route('/api/v1/mediaqc/report',methods=['GET'])
def getQcReport():
	print("here in printted")
	print('Ashok Commited')
	print('pravin commited')
	print('pravin commited again')

	videoJson=videoAnalysis()
	audioJson=audioAnalysis()


	return {"QC report":"url"}


if __name__ == '__main__':
    app.run(port='5001',host="0.0.0.0",debug=True)

