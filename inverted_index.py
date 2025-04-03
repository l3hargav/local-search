import os
import datetime
# from thefuzz import fuzz
# from thefuzz import process
from rapidfuzz import process
from klepto.archives import dir_archive


# TODO:
# Add more file types

# Get all data from given directory
# Store extracted data for searching
def get_data_from_dir(path: str) -> None:
    count = 0
    data = {}
    code_extensions = {'.py', '.c', '.lua', '.rs'}
    file_extensions = {'.txt'}

    for root, dirs, files in os.walk(path):
        for file in files:
            name, ext = os.path.splitext(os.path.join(root, file))
            if ext in code_extensions or ext in file_extensions:
                # Calls file_extractor on each file
                # And stores the file path and the data extracted in the dictionary
                data[str(count+1)] = {"path": os.path.join(root, file), "content": file_extractor(os.path.join(root, file))}
                count += 1

    with open("logs.txt", 'a') as f:
        ct = datetime.datetime.now()
        f.write(f"{ct}: Read {count} files\n")
    data_archive = dir_archive("data_store", data, serialized=True, cached=False, compression=2)
    # print(data_archive)

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

# Print the stored data archive
# Defaults to the first entry
def print_arch(index: int = 1) -> None:
    data = dir_archive("data_store", {}, compression=2, serialized=True)
    data.load()
    print("---------------------------------------")
    print("Total number of files in the archive: ", data.__len__())
    print("---------------------------------------")
    # print(data)
    for i in range(1, data.__len__()+1):
        print(i)
        print(data.get(str(i))['content'])
    with open('logs.txt', 'r') as f:
            content = f.read()


if __name__ == "__main__":
    path = os.path.expanduser("~/Documents/projects/test_dir/")
    get_data_from_dir(path)
    # print_arch()
    query = input("Enter search term: ")
    print_arch()
