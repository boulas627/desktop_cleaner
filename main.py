import sys
import time 
import logging 
from tkinter import filedialog
from Pathlib import Path

# this script will create directories for excel and powerpoint document types and place the correct file types into those folders 
# link to guide that I used: https://vivekhere.medium.com/how-i-organised-my-chaotic-folders-with-a-python-script-b70c92f01954

document_types = {
    "PowerPoints": ["pptx"], 
    "Excel": ["xml", "xlsx"], 
    "Videos": ["mp4", "mpeg", "mkv", "srt"],
    "Audio": ["mp3", "wav", "ogg"],
    "Compressed": ["zip", "tar", "rar"]
}

def get_directory(p): 
    return p 

def get_path(directory): 
    PATH = Path(directory)
    dest = PATH / "Organized"
    dest.mkdir(exist_ok=True)
    return PATH

def get_files(PATH): 
    files = []
    for i in PATH.iterdir(): 
        if i.is_file(): 
            files.append(i)

    return files 

def move_files(files): 
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



p = filedialog.askdirectory()
print(p)
