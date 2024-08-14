import sys
import time 
import logging 
import shutil
from tkinter import filedialog
from pathlib import Path

# this script will create directories for excel and powerpoint document types and place the correct file types into those folders 
# link to guide that I used: https://vivekhere.medium.com/how-i-organised-my-chaotic-folders-with-a-python-script-b70c92f01954


def get_path(directory): 
    PATH = Path(directory)
    # now setting our destination for organized files 
    dest = PATH / "Organized"
    dest.mkdir(exist_ok=True)
    return PATH

def get_files(PATH): 
    files = []
    for i in PATH.iterdir(): 
        if i.is_file(): 
            files.append(i)

    return files 

def get_dest(PATH): 
    dest = PATH / "Organized"
    dest.mkdir(exist_ok=True)
    return dest

def move_files(files, filetypes, dest): 
    for file in files: 
        done = 0 

        for k in filetypes.keys(): 
            if file.suffix[1:] in filetypes[k]:
                done = 1 
                destf = dest / f"{k}"
                destf.mkdir(exist_ok=True)
                shutil.move(str(file.resolve()), str(destf))

        if done != 1:
            continue 

def get_powerpoint_files(files): 
    return files 

filetypes = {
    "PowerPoints": ["pptx"], 
    "Excel": ["xml", "xlsx"], 
    "Videos": ["mp4", "mpeg", "mkv", "srt"],
    "Audio": ["mp3", "wav", "ogg"],
    "Compressed": ["zip", "tar", "rar"]
}



p = filedialog.askdirectory()
print("Our directory is: ", p)
path = get_path(p)

# print("Now getting our files")
# print(get_files(path))

files = get_files(path) 

destination = get_dest(path)
move_files(files, filetypes, destination)
