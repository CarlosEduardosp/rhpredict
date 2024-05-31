from sklearn.model_selection import train_test_split


def TreinoTeste(previsores: list, alvo: list):
    """
    :param previsores: dados para treino e teste.
    :param alvo: objetivo do treino e teste.
    :return: dados de treino e dados de teste.
    """

    x_treino, x_teste, y_treino, y_teste = train_test_split(previsores, alvo,
                                                            test_size=0.3, random_state=0)

    return {"x_treino": x_treino, "x_teste": x_teste, "y_treino": y_treino, "y_teste": y_teste}
