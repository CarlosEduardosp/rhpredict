import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from src.desenvolvimento.model.model_pessoa import Pessoa
from typing import Type, List
from src.analise_de_dados.previsores.previsores2 import Previsores2
from src.analise_de_dados.previsores.previsores_escalonado import Previsores_escalonado


def rodar_Algoritimo_escolhido(pessoa: Type[Pessoa]) -> List:

    # Configurar pandas para comportamento futuro
    pd.set_option('future.no_silent_downcasting', True)

    # Lendo o arquivo csv
    alvo = pd.read_csv('src/desenvolvimento/dados_csv/alvo.csv', sep=',', encoding='utf-8', header=None)
    previsores = pd.read_csv('src/desenvolvimento/dados_csv/previsores.csv', sep=',', encoding='utf-8', header=None)

    previsores2 = Previsores2(previsores)
    previsores_esc = Previsores_escalonado(previsores)

    # Convertendo 'alvo' para um array 1D se necessário
    if alvo.shape[1] == 1:  # Verifica se alvo tem apenas uma coluna
        alvo = alvo.values.ravel()  # Transforma em um array 1D
    else:
        raise ValueError("O arquivo 'alvo.csv' deve conter apenas uma coluna")

    # treino do algoritimo
    svc = make_pipeline(
        StandardScaler(),
        SVC(kernel='rbf', random_state=1, C=2)
    )
    svc.fit(previsores, alvo)

    # Exemplo de dados de entrada para previsão
    pessoa = np.array(pessoa.listar_atributos())

    # Transformando 'pessoa' para a forma correta (2D array)
    pessoa = pessoa.reshape(1, -1)

    # Fazendo a previsão
    resultado = svc.predict(pessoa)

    return resultado
