import os
import datetime
from thefuzz import fuzz
from thefuzz import process
from klepto.archives import dir_archive


# TODO:
# Add more file types

# Get all data from given directory
# Store extracted data for searching
def get_data_from_dir(path: str) -> None:
    count = 0
    data = {}
    extensions = {'.py', '.txt', '.c', '.lua', '.rs'}
    for root, dirs, files in os.walk(path):
        for file in files:
            name, ext = os.path.splitext(os.path.join(root, file))
            if ext in extensions:
                # Calls file_extractor on each file
                # And stores the file path and the data extracted in the dictionary
                data[str(count+1)] = {"path": os.path.join(root, file), "content": file_extractor(os.path.join(root, file))}
                count += 1
    # for key in data:
    #     print(key, ":", data[key]["content"][:10])

    with open("logs.txt", 'a') as f:
        ct = datetime.datetime.now()
        f.write(f"{ct}: Read {count} files\n")
    data_archive = dir_archive("data_store", data, serialized=True, cached=False, compression=2)
    # print(data_archive['1'])

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

# def search(words: str = ''):
#     data = dir_archive("data_store", {}, serialized=True)
#     data.load()
#     print(data)

if __name__ == "__main__":
    path = os.path.expanduser("~/Documents/projects/test_dir/")
    get_data_from_dir(path)
    # search()
