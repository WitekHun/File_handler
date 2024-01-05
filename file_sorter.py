import os
from pathlib import Path
import shutil
import sys
dir_list=[]
images_list=[]
docs_list=[]
audio_list=[]
video_list=[]
archives_list=[]
images_extensions=['.jpeg', '.png', '.jpg', '.svg']
video_extensions=['.avi', '.mp4', '.mov', '.mkv']
docs_extensions=['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']
audio_extensions=['.mp3', '.ogg', '.wav', '.amr']
archive_extensions=['.zip', '.gz', '.tar']


def files_list(dir):
    directory=Path(dir)
    sorted_path=(Path(sys.argv[1])).parent
    logs_path=os.path.join(sorted_path, "Logs")
    sorted_dir=os.path.join(sorted_path, "Sorted")
    images_dir=os.path.join(sorted_dir, "Images")
    video_dir=os.path.join(sorted_dir, "Video")
    docs_dir=os.path.join(sorted_dir, "Documents")
    audio_dir=os.path.join(sorted_dir, "Audio")
    all_list=os.listdir(sys.argv[1])
    with open(f'{logs_path}/lista.txt', 'a') as fh:
        fh.write('Lista plików \n')
    with open(f"{logs_path}/first_list.txt","a") as fh:
                fh.write(f"Pliki i foldery w Mixed os.listdir(sys.argv[1]): {str(all_list)} \n")
    for i in directory.iterdir(): 
        p=Path(i)

        if i.is_dir():
            if i not in dir_list:
                dir_list.append(p)
                with open(f"{logs_path}/direct_list.txt","a") as fh:
                    fh.write(f'{dir_list} \n')
            files_list(str(p))
        else:
            with open(f"{logs_path}/file_list.txt", 'a') as fh:
                fh.write(f'{os.path.join(directory, i)} Is file \n')
            if p.suffix in images_extensions:
                images_file(os.path.join(directory, i), images_dir)
                with open(f'{logs_path}/lista.txt', 'a') as fh:
                    fh.write(f'{str(i)} \n')
            elif p.suffix in video_extensions:
                video_file(os.path.join(directory, i), video_dir)
                with open(f'{logs_path}/lista.txt', 'a') as fh:
                    fh.write(f'{str(i)} \n')
            elif p.suffix in docs_extensions:
                docs_file(os.path.join(directory, i), docs_dir)
                with open(f'{logs_path}/lista.txt', 'a') as fh:
                    fh.write(f'{str(i)} \n')
            elif p.suffix in audio_extensions:
                docs_file(os.path.join(directory, i), audio_dir)
                with open(f'{logs_path}/lista.txt', 'a') as fh:
                    fh.write(f'{str(i)} \n')
    for i in set(dir_list):
        if i.is_dir() and len([i for i in i.iterdir()])==0:
            os.rmdir(i)

    """
    for file in images_list:
        with open(f"{logs_path}/lista_2.txt", 'a') as fh:
            fh.write(f"{str(file)} \n")
        shutil.copy(file, images_dir)
    """


def images_file(file, directory):
    images_list.append(file)
    shutil.move(file, directory)

def docs_file(file, directory):
    docs_list.append(file)
    shutil.move(file, directory)

def audio_file(file, directory):
    audio_list.append(file)
    shutil.move(file, directory)

def video_file(file, directory):
    video_list.append(file)
    shutil.move(file, directory)

def archives_file(file, directory):
    archives_list.append(file)
    shutil.move(file, directory)

def mk_dir(dir, directory):
    if directory in os.listdir(dir):
        print(f"{dir}/{directory} already exist")
    else:
        os.mkdir(Path(f"{dir}/{directory}"))

if __name__=="__main__":
    mk_dir((Path(sys.argv[1])).parent, "Logs")
    sorted_path=os.path.join(((Path(sys.argv[1])).parent), "Sorted")
    mk_dir((Path(sys.argv[1])).parent, "Sorted")
    mk_dir(sorted_path, "Images")
    mk_dir(sorted_path, "Videos")
    mk_dir(sorted_path, "Documents")
    mk_dir(sorted_path, "Audio")
    mk_dir(sorted_path, "Archives")
    files_list(sys.argv[1])
