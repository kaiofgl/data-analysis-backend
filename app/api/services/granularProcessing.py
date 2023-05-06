import config as Config
from flask import jsonify

import json

import datetime
import pandas as pd

from api.utils.processing import exceptColumn, exceptionToProcess, makeSugestion, readFile

from nltk.corpus import stopwords

class GranularProcessingService:
    @staticmethod
    def index(data, column):
        try:

            if (column == 'Qual a sua data de nascimento?'):
                birthdate = {}
                birthdate['data'] = GranularProcessingService.birthdate(data)
                birthdate['type_suggestion'] = "bar"

                print(birthdate) 

                return birthdate

            if (column == "Escreva algumas linhas sobre sua história e seus sonhos de vida."):
                dreams = {}
                dreams['data'] = GranularProcessingService.dreams(data)
                dreams['type_suggestion'] = "word_cloud"
                return dreams

            if (column == "Qual a empresa que você está contratado agora?"):
                work = {}
                work['data'] = GranularProcessingService.work(data)
                work['type_suggestion'] = "bar"

                return work

        except:
            return False

    @staticmethod
    def birthdate(data):
        df = pd.DataFrame({'data_nascimento': data})
        df['data_nascimento'] = pd.to_datetime(df['data_nascimento'], unit='ms')
        df['idade'] = (datetime.datetime.now() - df['data_nascimento']).astype('timedelta64[Y]')

        faixas_etarias = pd.cut(df['idade'], bins=range(18, 100, 5))

        contagens = faixas_etarias.value_counts().to_dict()

        contagens_str = {}
        for faixa_etaria, contagem in contagens.items():
            if (contagem > 0):
                faixa_etaria_str = f"{faixa_etaria.left}-{faixa_etaria.right} anos"
                contagens_str[faixa_etaria_str] = contagem
        
        return contagens_str

    @staticmethod
    def dreams(data):
        dream_string = ' '.join(data.tolist())
        dream_list = dream_string.lower().split()

        stop_words = set(stopwords.words('portuguese'))
        dream_list = [word for word in dream_list if word not in stop_words]

        word_counts = pd.Series(dream_list).value_counts().to_dict()

        return word_counts

    @staticmethod
    def work(data):

        stripped_works = []

        listOfData = data.to_list()
        for item in listOfData:
            if item is not None:
                stripped_works.append(item.strip())
        
        works = pd.Series(stripped_works).value_counts().to_dict()

        return works