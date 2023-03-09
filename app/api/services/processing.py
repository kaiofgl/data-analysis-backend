import config as Config

import json

import pandas as pd

class ProcessingService:
    @staticmethod
    def single(filename, column):
        try:
            with open(Config.ROOT_DIR_OUTPUT + filename, 'r') as f:
                jsonFile = json.load(f)
            df = pd.DataFrame(jsonFile)

            processedColumn = df[column].value_counts()

            processedColumnToJson = processedColumn.to_json()

            return processedColumnToJson
        except:
            return False
