from sklearn.preprocessing import LabelEncoder
import numpy as nd


def Previsores2(df: list):

    """
    :return: previsores2 = conjunto de variáveis previsoras com as variáveis categóricas transformadas
    em numéricas pelo labelencoder.
    """

    # Exclui a coluna de número que for passado.
    df = df.drop(df.columns[2], axis=1)

    previsores2 = df.iloc[:, 0:7].values

    # acertando o valor da coluna
    corrigindo_valor_coluna = 5 - 1
    corrigindo_valor_coluna2 = 6 - 1

    previsores2[:, 0] = LabelEncoder().fit_transform(previsores2[:, 0])
    previsores2[:, corrigindo_valor_coluna] = LabelEncoder().fit_transform(previsores2[:, corrigindo_valor_coluna])
    previsores2[:, corrigindo_valor_coluna2] = LabelEncoder().fit_transform(previsores2[:, corrigindo_valor_coluna2])

    return previsores2
