import os
from pathlib import Path
import shutil
import sys
file_list=[]
dir_list=[]
images_list=[]
docs_list=[]
audio_list=[]
video_list=[]
archives_list=[]

def files_list(dir_path):
    p=Path(dir_path)
    for i in p.iterdir(): 
        if i.is_file():
            if i.suffix==".jpg":
                images_list.append(i)
            else:
                file_list.append(i)
        else:
            if i.suffix!=".git":
                files_list(os.path.join(p,i))
                dir_list.append(i)
            print(dir_list)
    with open('list.txt', 'a') as fh:
        fh.write(f'Directory List: {dir_list} \n Images List: {images_list} \n File list: {file_list} \n')
    
if __name__=="__main__":
    files_list('/Users/witekhungendorfer/Desktop/GoIT/Projects/File_handler/')