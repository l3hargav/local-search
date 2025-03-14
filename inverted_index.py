import os
import sys
from klepto.archives import dir_archive

path = os.path.expanduser("~/Documents/projects/test_dir/")

# Get all data from given directory
def get_data_from_dir(path):
    data = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            name, ext = os.path.splitext(os.path.join(root, file))
            # TODO:
            # Add more file types
            # Put in some kind of data structure like a set or list
            if ext == '.py' or ext == '.txt' or ext == '.rs' or ext == '.c' or ext == '.lua':
                # Calls file_extractor on each file
                # And stores the file path and the data extracted in the dictionary
                data[os.path.join(root, file)] = file_extractor(os.path.join(root, file))
    return data

def file_extractor(file_path):
    # Get file content
    try:
        with open(file_path, 'r') as f:
            content = f.read()
    except OSError:
        with open("logs.txt", 'a') as f:
            f.write(f"ERROR: File could not be read: {file_path}\n")
            return f'Error occured in reading {file_path}: Check logs'
    return content


if __name__ == "__main__":
    data = get_data_from_dir(path)
    print([key for key in data])
    print(len(data))
