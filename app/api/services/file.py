import config as Config

import os, json

import pandas as pd

from api.utils.processing import exceptColumn, exceptionToProcess, makeSugestion, readFile
import uuid

class FileService:
    @staticmethod
    def upload(file, filename):
        try:
            fileReaded = readFile(file)
            fileExtension = file.filename.split('.')[-1]

            json = fileReaded.to_json(orient='records')

            fileHash = uuid.uuid4().hex[:8]

            if not os.path.isdir(Config.ROOT_DIR_OUTPUT):
                os.mkdir(Config.ROOT_DIR_OUTPUT)
            with open(Config.ROOT_DIR_OUTPUT + "/" + filename + "_" + fileHash + ".json", 'w') as fileOpened:
                fileOpened.write(json)

            data = {}
            data['filename'] = filename + "_" +fileHash
            data['filename_friendly'] = filename
            data['extension'] = fileExtension

            return data

        except:
            return False
    @staticmethod
    def getFile(filename):
        try:
            with open(Config.ROOT_DIR_OUTPUT + filename + ".json", 'r') as f:
                jsonFile = json.load(f)
            return jsonFile
        except:
            return False