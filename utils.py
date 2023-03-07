import pandas as pd

def getStructureFromJson(item):
    structure = []
    for key, value in item.items():
        structure.append(key)
    return structure;

def readFile(file):
    fileReaded = pd.read_excel(file)
    return fileReaded;

def saveToJson(file, path):
    json = file.to_json(orient='records')

    with open(path, 'w') as file:
        file.write(json)

    return json