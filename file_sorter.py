import os
from pathlib import Path
import shutil
import sys
images_list=[]
docs_list=[]
audio_list=[]
video_list=[]
archives_list=[]

def files_list(dir):
    directory=Path(dir)
    logs=os.path.join(sys.argv[1], 'Logs')
    sorted_dir=os.path.join(sys.argv[1], "Sorted")
    images_dir=os.path.join(sorted_dir, "Images")
    docs_dir=os.path.join(sorted_dir, "Documents")
    all_list=os.listdir(sys.argv[1])
    with open('lista.txt', 'a') as fh:
        fh.write('Lista plików \n')
    with open("first_list.txt","a") as fh:
                fh.write(f"{str(all_list)} \n")
    #print(f"ITERDIR: {directory.iterdir()}!!!!")
    for i in os.listdir(directory): 
        p=Path(f'{directory}/{i}')
        print(p)
        if p.is_dir() and str(i).endswith!="Sorted":
            with open("dir_list.txt","a") as fh:
                fh.write(f'{os.path.join(directory, i)} \n')
            #print(f'{os.path.join(directory, i)} is directory')
            files_list(os.path.join(directory, i))
        else:
            with open("file_list.txt", 'a') as fh:
                fh.write(f'{os.path.join(directory, i)} Is file \n')
            if i.endswith('.jpg'):
                #image_dir=os.path.join(os.path.join(path, "Sorted"),"Images")
                images_file(os.path.join(directory, i), images_dir)
                #file_name=str(i).split('/')
                with open('lista.txt', 'a') as fh:
                    fh.write(f'{str(i)} \n')
                    #fh.write(f'{file_name[-1]} \n')
    print(f'Lista obrazów: {images_list}')
    
    for file in images_list:
        with open("lista_2.txt", 'a') as fh:
            fh.write(f"{str(file)} \n")
        shutil.copy(file, images_dir)


def images_file(file, directory):
    images_list.append(file)
    #shutil.copy(file, directory)
    #print(f'Source: {source}, Destination: {destination}')
    #print(f'LISTA OBRAZOW: {len(images_list)} !!')

def docs_file(file, directory):
    docs_list.append(file)
    shutil.move(file, "Documents")

def audio_file(file, directory):
    audio_list.append(file)
    shutil.move(file, "Audio")

def video_file(file, directory):
    video_list.append(file)
    shutil.move(file,"Video")

def archives_file(file, directory):
    pass

def mk_dir(dir, directory):
    if directory in os.listdir(dir):
        print(f"{dir}/{directory} already exist")
    else:
        os.mkdir(f"{dir}/{directory}")

if __name__=="__main__":
    #files_list("/Users/witekhungendorfer/Desktop/GoIT/Projects/File_handler")
    
    mk_dir(sys.argv[1], "Sorted")
    mk_dir(os.path.join(sys.argv[1], "Sorted"), "Images")
    files_list(sys.argv[1])
    #p=Path(r"")