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
