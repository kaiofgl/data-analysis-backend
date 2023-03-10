import config as Config

import os, json

import pandas as pd

class FileService:
    @staticmethod
    def upload(file, filename):
        try:
            fileReaded = pd.read_excel(file)
            json = fileReaded.to_json(orient='records')

            if not os.path.isdir(Config.ROOT_DIR_OUTPUT):
                os.mkdir(Config.ROOT_DIR_OUTPUT)
            with open(Config.ROOT_DIR_OUTPUT + "/" + filename + ".json", 'w') as fileOpened:
                fileOpened.write(json)

            return "uploaded"
        except:
            return False
    @staticmethod
    def getFile(filename):
        try:
            with open(Config.ROOT_DIR_OUTPUT + filename, 'r') as f:
                jsonFile = json.load(f)
            return jsonFile
        except:
            return False