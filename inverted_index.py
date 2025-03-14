import os
import datetime
from typing import Dict
from klepto.archives import dir_archive


# TODO:
# Add more file types
# Put in some kind of data structure like a set or list for storing file types

# Get all data from given directory
# Store extracted data for searching
def get_data_from_dir(path: str) -> None:
    count = 0
    data = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            name, ext = os.path.splitext(os.path.join(root, file))
            if ext == '.py' or ext == '.txt' or ext == '.rs' or ext == '.c' or ext == '.lua':
                # Calls file_extractor on each file
                # And stores the file path and the data extracted in the dictionary
                data[os.path.join(root, file)] = file_extractor(os.path.join(root, file))
                count += 1
    with open("logs.txt", 'a') as f:
        ct = datetime.datetime.now()
        f.write(f"{ct}: Read {count} files\n")
    data_archive = dir_archive("data_store", data, cached=False, compression=2)

# Get file content
def file_extractor(file_path: str) -> str:
    try:
        with open(file_path, 'r') as f:
            content = f.read()
    except OSError:
        with open("logs.txt", 'a') as f:
            f.write(f"ERROR: File could not be read: {file_path}\n")
            return f'Error occured in reading {file_path}: Check logs'
    return content



if __name__ == "__main__":
    path = os.path.expanduser("~/Documents/projects/test_dir/")
    get_data_from_dir(path)
