import os
import pathlib
from klepto.archives import dir_archive

path = os.path.expanduser("~/Documents/projects/test_dir/")

# for root, dirs, file in os.walk(path):
#     print(root)
#     print(dirs)
#     print(file)


data = {}
def get_data_from_files(path):
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            get_data_from_files(dir)

        for file in files:
            name, ext = os.path.splitext(os.path.join(path, file))
            print(name)
            print(ext)
            # Add more file types
            if ext == '.py' or ext == '.txt' or ext == '.rs' or ext == '.c' or ext == '.lua':
                # Do something with the file
                data[file] = ''

def file_extractor(file):
    pass 

get_data_from_files(path)
print(data)
