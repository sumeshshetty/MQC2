import ffmpeg
import sys
from pprint import pprint
import subprocess,shlex	
import os
import re

def blackFrame(file_path):
    try:
        print("Excecuting blackFrame")
        command=f'ffmpeg -i {file_path} -vf "blackdetect=d=0.05:pix_th=0.10" -an -f null - '
        li=shlex.split(command)    # split command and store in list seprated by '',


        #command call by subprocess 
        output=subprocess.run(li,stdout=subprocess.PIPE,stderr=subprocess.PIPE)  
        stdout=output.stdout
        stderror=output.stderr

        #convrerting byte into string
        result=stderror.decode("utf-8")

        
        if "blackdetect @" not in result:
            print("not found details")
            return {"Black Frame":"No Black Frame Detected"}

        ff_list=result.split('\n')

        refined_list=[]
        for item in ff_list:

        	if "[blackdetect @" in item:
        		item=item.split(']')[1]
        		refined_list.append(item)

        final_list=[]
        new_dict={}
        count=0


        tmp_list=[]
        for item in refined_list:
        	tmp_list.extend(item.split(" "))
        tmp_list = filter(lambda item: item, tmp_list)

        for item in tmp_list:
            count=count+1
            
            
            if count%3==0:
                key=item.split(":")[0].replace('black_','')
                value=item.split(":")[1]
                
                new_dict.update({key:value})
                final_list.append(new_dict)
                
                new_dict={}

            else:
                key=item.split(":")[0].replace('black_','')
                value=item.split(":")[1]
                
                new_dict.update({key:value})
        
    except Exception as err:
        print(f"Error in blackFrame : {err}")
        final_list=""
    if final_list:
        print(f"blackFrame final_list: {final_list}")
        return {"Black Frame":final_list}