from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


def Previsores3(previsores2):
    """
    :param previsores2:
    :return: previsores3 = conjunto de variáveis previsoras transformadas pelo
    labelencoder e onehotencoder, sem escalonar.
    """

    previsores3 = ColumnTransformer(transformers=[('OneHot', OneHotEncoder(), [0,5,6])],
                                    remainder='passthrough').fit_transform(previsores2)

    return previsores3