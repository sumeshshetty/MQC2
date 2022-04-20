import ffmpeg
import sys
from pprint import pprint
import subprocess,shlex	
import os
import re

def freezeFrame(file_path):
    try:
        print("Excecuting freezeFrame")

        command=f'ffmpeg -i {file_path} -vf "freezedetect=n=0.01:d=2,metadata=mode=print:file=freeze.txt"  -map 0:v:0 -f null -'
        li=shlex.split(command)    # split command and store in list seprated by '',


        #command call by subprocess 
        output=subprocess.run(li,stdout=subprocess.PIPE,stderr=subprocess.PIPE)  
        stdout=output.stdout
        stderror=output.stderr

        #convrerting byte into string
        result=stderror.decode("utf-8")

        if "freezedetect @" not in result:
            print("not found detaisl")
            return {"Freeze Frame":"No Freeze Frame Detected"}
        #extract data bettween two charcaters
        start='lavfi.freezedetect.'
        end='overhead: unknown'

        freeze_details=result[result.find(start)+len(start):result.rfind('frame=')]
        list_details=freeze_details.split('\n')
        list_details = filter(lambda item: item, list_details)




        refined_list=[]
        for item in list_details:
            if "freezedetect @" in item:
                item=item.split("_")[-1]
                refined_list.append(item)
            else:
                item=item.replace("freeze_","")
                refined_list.append(item)


        final_list=[]
        new_dict={}
        count=0

        for item in refined_list:
            count=count+1
            key=item.split(":")[0]
            value=item.split(":")[1]
            
            if count%3==0:
                new_dict.update({key:value})
                final_list.append(new_dict)
                new_dict={}
            else:
                new_dict.update({key:value})
                
        os.remove("freeze.txt")
    except Exception as err:
        print(f"Error in freezeFrame : {err}")
        final_list="Exception: No Freeze Frame Detected"

    print(f"Freeze Frame final_list: {final_list}")

    return {"Freeze Frame":final_list}

        





