import os
from klepto.archives import dir_archive

path = os.path.expanduser("~/Documents/projects/test_dir/")

data = {}
# Get all data from given directory
def get_data_from_dir(path):
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            get_data_from_dir(os.path.join(root, dir))

        for file in files:
            name, ext = os.path.splitext(os.path.join(path, file))
            # TODO:
            # Add more file types
            if ext == '.py' or ext == '.txt' or ext == '.rs' or ext == '.c' or ext == '.lua':
                # Calls file_extractor on each file
                # And stores the file path and the data extracted in the dictionary
                data[os.path.join(root, file)] = file_extractor(os.path.join(root, file))

def file_extractor(file_path):
    # Get file content
    with open(file_path, 'r') as f:
        content = f.read()
    return content


get_data_from_dir(path)
print(len(data))
for key in data:
    print(key)
