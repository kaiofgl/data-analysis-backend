import pandas as pd
import datetime

def makeSugestion(data):
    size = len(data)

    if (size >= 0 and size <= 3):
        return "pie"

    if (size > 3 ):
        return "bar"

    # if (size > 5):
    #     return "column"

def readFile(file):
    fileExtension = file.filename.split('.')[-1]

    if (fileExtension == "xlsx"):
        fileReaded = pd.read_excel(file)
        return fileReaded
    elif (fileExtension == "csv"):
        fileReaded = pd.read_csv(file)
        return fileReaded
    elif (fileExtension == "json"):
        fileReaded = pd.read_json(file)
        return fileReaded
    else:
        return False


def exceptColumn(column):
    listOfException = [
        'ID',
        'Hora de início',
        'Hora de conclusão',
        'Email',
        'Nome',
        'Informe o número do seu RA.' 
    ]

    if (column) in listOfException:
        return False
    return True

def exceptionToProcess(column):
    listOfException = [
        'Qual a sua data de nascimento?',
        'Escreva algumas linhas sobre sua história e seus sonhos de vida.'
    ]

    if (column) in listOfException:
        return column
    return False
