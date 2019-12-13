from pathlib import Path
import os
import xmltodict, requests
from datetime import datetime

def files_to_send(): # this function is used to get a list of all the files that we want to send from the 'files' directory.

    # set the 'files' sub-folder as the current working directory (cwd)
    cwd = os.chdir('./files')
    cwd = os.getcwd()

    # creates an empty list to store all the files in
    total_files=[] # create a list that can store the file name values
    entries = Path(cwd) # sets the directory to iterate through

    # a loop that will incrementally add all files names to the 'total_files' list
    for entry in entries.iterdir():
        total_files.append(entry.name)

    # return the 'total_files' list from the function
    return total_files

def error_log(f1, f2): # this function writes to a log file any differences (plus a timestamp) between the files
    print(f'Files {f1} and {f2} dont match')
    f = open("error_log.txt", "a")
    f.write(f'Files {f1} and {f2} dont match - {datetime.now()} \n')
    f.close()