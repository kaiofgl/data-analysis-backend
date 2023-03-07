from utils import getStructureFromJson, readFile, saveToJson

import json
import pandas as pd

def dataFrameGroupBy():
    print("datagroup")

    with open('output.json', 'r') as f:
        dataOutputJson = json.load(f)

    df = pd.DataFrame(dataOutputJson)

    groupByData = df.groupby(['Idade', 'Gênero']).size()

    unstacked = groupByData.unstack()

    toDict = unstacked.to_dict()

    processedDataToJson = json.dumps(toDict)

    print(processedDataToJson)

def getJsonFromFile():
    path = "./database/BD.xlsx";

    file = readFile(path);

    if not file.empty:
        jsonString = saveToJson(file, "output.json")

    dataFrameGroupBy()

getJsonFromFile();