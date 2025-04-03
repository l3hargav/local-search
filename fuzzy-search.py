from rapidfuzz import process
from klepto.archives import dir_archive

# TODO:
# Search for an input word in the archive
# -- Fuzzy search
def search(query: str = ''):
    data = dir_archive("data_store", {}, compression=2, serialized=True)
    data.load()
    choices = []
    file_names = []
    for i in range(1, data.__len__()+1):
        choices.append(data.get(str(i))['content'])
        file_names.append(data.get(str(i))['path'])

    outputs = process.extract(query, choices)
    idx = outputs[0][2]
    print(file_names[idx])


if __name__ == "__main__": 
    query = input("Enter search term: ")
    search(query)
