from pathlib import Path
import os
import xmltodict, requests, datetime

def files_to_send():

    # set the 'files' sub-folder as the current working directory (cwd)
    cwd = os.chdir('./files')
    cwd = os.getcwd()

    # return all files in the files directory
    total_files=[] # create a list that can store the file name values
    entries = Path(cwd) # sets the directory to iterate through

    # a loop that will incrementally add all files names to the 'total_files' list
    for entry in entries.iterdir():
        total_files.append(entry.name)

    return total_files

def parse_files(insert_file):
    # parse a copy of the file that we sent to the endpoint
    with open(insert_file) as fd:
        doc = xmltodict.parse(fd.read())
        return doc

# the function to retrieve the contents of the file from the end-point
def get(fn):
    to_compare = requests.get(fn)
    return to_compare

# writes to a log file any differences (with a timestamp) between the files
def error_log(f1, f2):
    print(f'Files {f1} and {f2} dont match')
    f = open("error_log.txt", "a")
    f.write(f'Files {f1} and {f2} dont match - {datetime.now()} \n')
    f.close()