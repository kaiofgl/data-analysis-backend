import config as Config

import json

import pandas as pd

class ProcessingService:
    @staticmethod
    def single(filename, column, normalizeColumn):

        try:
            with open(Config.ROOT_DIR_OUTPUT + filename + ".json", 'r') as f:
                jsonFile = json.load(f)

            df = pd.DataFrame(jsonFile)
            processedColumn = df[column].value_counts(normalize=normalizeColumn)
            processedColumnToJson = processedColumn.to_json()

            return processedColumnToJson
        except:
            return False

    @staticmethod
    def double(filename, first_column, second_column):
        try:
            with open(Config.ROOT_DIR_OUTPUT + filename + ".json", 'r') as f:
                jsonFile = json.load(f)

            df = pd.DataFrame(jsonFile)

            groupByData = df.groupby([first_column, second_column]).size()

            unstacked = groupByData.unstack().fillna(0)

            toDict = unstacked.to_dict()

            processedDataToJson = json.dumps(toDict)

            return processedDataToJson
        except:
            return False

    @staticmethod
    def structure(filename):
        try:
            with open(Config.ROOT_DIR_OUTPUT + filename + ".json", 'r') as f:
                jsonFile = json.load(f)
            structure = []
            file = jsonFile[0]
            for key in file.keys():
                structure.append(key)
            return structure
        except:
            return False