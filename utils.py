import pandas as pd

import os, json

uploadsPath = "./outputs"

def readFile(file):
    fileReaded = pd.read_excel(file)
    return fileReaded;

def getStructureFromJson(items):
    structure = []
    file = items[0]
    for key in file.keys():
        structure.append(key)
    return structure

def convertFileToJson(file):
    json = file.to_json(orient='records')
    if not os.path.isdir(uploadsPath):
        os.mkdir(uploadsPath)

    with open(uploadsPath + "/" + "fdsajewjgl341.json", 'w') as file:
        file.write(json)

def openJsonFile(path):
    try:
        with open(uploadsPath + "/" + path, 'r') as f:
            jsonFile = json.load(f)
        return jsonFile
    except:
        return False