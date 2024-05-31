import pandas as pd
from sklearn.preprocessing import StandardScaler


def Previsores_escalonado(previsores: list):
    """
    previsores_escalonado = conjunto de variáveis previsoras com as variáveis categóricas transformadas
    em numéricas, escalonada.

    """

    previsores_escalonado = StandardScaler().fit_transform(previsores)
    #print(previsores_escalonado)

    previsoresdf = pd.DataFrame(previsores_escalonado)
    #print(previsoresdf)

    return previsores_escalonado
