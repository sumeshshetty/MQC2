import cv2 
blurDict=[]



def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)



def getFrame(sec,vidcap): 
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000) 
    hasFrames,image = vidcap.read() 
    
    if hasFrames: 
    
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm = cv2.Laplacian(gray, cv2.CV_64F).var()
        time_c=convert(sec)
        #count+=1
        if fm < 300:
            text = "Blurry"
            #print ("image is blurry",fm,time_c)
            #uncomment for validation
            #cv2.imwrite("tmp/frame "+str(sec)+" sec.jpg", image)
            blurDict.append({"blur frame":time_c})
        
    return hasFrames ,blurDict
def blurDetect(qc_details):
    url=qc_details['video_url']

    vidcap = cv2.VideoCapture(url) 
    sec = 0 
    frameRate = 1#it will capture image in each 0.5 second 
    success,blurDict = getFrame(sec,vidcap) 
    while success: 
        sec = sec + frameRate 
        sec = round(sec, 2) 
        success,blurDict = getFrame(sec,vidcap)


    print("final list:",blurDict)
    return {"blur Detection":blurDict}



