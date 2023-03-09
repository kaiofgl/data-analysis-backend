from utils import (getStructureFromJson, 
    readFile,
    convertFileToJson, 
    openJsonFile
)

import json
import pandas as pd

uploadsPath = "./outputs"

def dataFrameGroupBy():
    print("datagroup")

    with open('output.json', 'r') as f:
        dataOutputJson = json.load(f)

    df = pd.DataFrame(dataOutputJson)

    groupByData = df.groupby(['Idade', 'Gênero']).size()

    unstacked = groupByData.unstack()

    toDict = unstacked.to_dict()

    processedDataToJson = json.dumps(toDict)

    return processedDataToJson

def dataFrameSingle(file, column):

    with open(uploadsPath + "/" + file, 'r') as f:
        dataOutputJson = json.load(f)

    df = pd.DataFrame(dataOutputJson)

    processedColumn = df[column].value_counts()

    processedColumnToJson = processedColumn.to_json()
    return processedColumnToJson


    # return processedDataToJson

def getStructure(request):
    file = request['filename']
    column = request['column']
    file = openJsonFile(file)
    return(json.dumps(getStructureFromJson(file)))
    # return(dataFrameSingle(file, column))
    


def uploadFile(file):
    fileReaded = readFile(file);
    convertFileToJson(fileReaded);
    return True

def getFile(request):
    file = openJsonFile(request['filename'])
    if(file):
        return file
    return False

