import config as Config

import json
class FileService:
    @staticmethod
    def getFile(filename):
        try:
            with open(Config.ROOT_DIR_OUTPUT + filename, 'r') as f:
                jsonFile = json.load(f)
            return jsonFile
        except:
            return False