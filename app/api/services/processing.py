import config as Config
from flask import jsonify

import json

import pandas as pd

class ProcessingService:
    @staticmethod
    def all(filename):
        try:
            with open(Config.ROOT_DIR_OUTPUT + filename + ".json", 'r') as f:
                jsonFile = json.load(f)

            dataProcessed = {}
            structure = ProcessingService.structure(filename)

            for column in structure:
                df = pd.DataFrame(jsonFile)

                if (df[column].astype(str).str.contains(';').any() and column != 'Qual seu horário de trabalho?'):
                    df[column] = df[column].str.rstrip(';')
                    df = df.assign(**{column: df[column].str.split(';')}).explode(column)

                    contagens = df[column].value_counts(dropna=True).to_dict()
                    dataProcessed[column] = contagens
                    print(contagens)

                else:
                    processedColumn = df[column].value_counts()
                    dataProcessed[column] = processedColumn.to_dict()

            return json.dumps(dataProcessed)
        except:
            return False

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

    @staticmethod
    def preStructure(file):

        try:
            fileReaded = pd.read_excel(file)
            jsonString = fileReaded.to_json(orient='records')

            jsonConverted = json.loads(jsonString) 


            structure = []
            for key in jsonConverted[0].keys():
                structure.append(key)

            return structure
        except:
            return False

    @staticmethod
    def columnPreProcessing(file, column):
        try:
            fileReaded = pd.read_excel(file)
            jsonString = fileReaded.to_json(orient='records')

            jsonConverted = json.loads(jsonString) 

            df = pd.DataFrame(jsonConverted)

            if (df[column].astype(str).str.contains(';').any() and column != 'Qual seu horário de trabalho?'):

                df[column] = df[column].str.rstrip(';')
                df = df.assign(**{column: df[column].str.split(';')}).explode(column)

                contagens = df[column].value_counts(dropna=True).to_dict()

                processedColumnToJson = json.dumps(contagens)

            else:
                processedColumn = df[column].value_counts()
                processedColumnToJson = processedColumn.to_json()

            return processedColumnToJson
        except:
            return False