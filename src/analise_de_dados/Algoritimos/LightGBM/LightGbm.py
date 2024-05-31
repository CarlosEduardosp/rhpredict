from sklearn.metrics import accuracy_score, confusion_matrix
from datetime import datetime
from src.analise_de_dados.treino_e_teste.treino_e_teste import TreinoTeste
from sklearn.model_selection import KFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import lightgbm as lgb


def Algoritimo_LightGBM(dados_treino_e_teste: dict):
    x_treino = dados_treino_e_teste['x_treino']
    y_treino = dados_treino_e_teste['y_treino']
    x_teste = dados_treino_e_teste['x_teste']
    y_teste = dados_treino_e_teste['y_teste']

    # Dataset para treino
    dataset = lgb.Dataset(x_treino, label=y_treino)

    # Parâmetros
    parametros = {'num_leaves': 250,  # número de folhas
                  'objective': 'binary',  # classificação Binária
                  'max_depth': 2,
                  'learning_rate': .05,
                  'max_bin': 100}

    lgbm = lgb.train(parametros, dataset, num_boost_round=200)

    # Marcação do tempo de execução
    inicio = datetime.now()
    lgbm = lgb.train(parametros, dataset)
    fim = datetime.now()

    tempo = fim - inicio

    previsoes_lgbm = lgbm.predict(x_teste)

    print(previsoes_lgbm.shape)

    # Quando for menor que 5 considera 0 e quando for maior ou igual a 5 considera 1
    for i in range(0, 634):
        if previsoes_lgbm[i] >= .5:
            previsoes_lgbm[i] = 1
        else:
            previsoes_lgbm[i] = 0

    print(f'acurácia dados de teste é de: {accuracy_score(y_teste, previsoes_lgbm) * 100.0:.2f}%')

    # matrix de confusão
    matriz = confusion_matrix(y_teste, previsoes_lgbm)
    # print('matriz de confusão', matriz)

    # avaliação do algoritimo dados de treino.
    previsores_naive = lgbm.predict(x_treino)
    # print('teste com naive bayes', previsores_naive)
    # print('dados de x treino', x_treino)

    print(previsores_naive.shape)

    # verificando a acurácia.
    print(f'acurácia dados de treino é de: {accuracy_score(y_treino, previsores_naive) * 100:.2f}%')


def avaliarLightGBM(todos_os_previsores: list, alvo: list, ):
    print('----------------------------------------------')
    print('Testando e Avaliando LIGHTGBM: ')
    print('----------------------------------------------')

    # dados de treino de todos os previsores de uma vez.
    for i in todos_os_previsores:
        print(f'Teste com {i['id']}')

        dados_treino_e_teste = TreinoTeste(i['previsores'], alvo)
        # print(dados_treino_e_teste)

        # aplicando o algoritimo XGboost.
        response = Algoritimo_LightGBM(dados_treino_e_teste)

        # validação cruzada

        # Separando os dados em folds
        kfold = KFold(n_splits=30, shuffle=True, random_state=5)

        # Criando o modelo
        modelo = make_pipeline(
            StandardScaler(),
            lgb.LGBMClassifier(num_leaves=250, objective='binary',
                               max_depth=2, learning_rate=.05, max_bin=100)
        )
        resultado = cross_val_score(modelo, i['previsores'], alvo, cv=kfold)

        # Usamos a média e o desvio padrão
        print(f"Validação Cruzada, Acurácia Média: {resultado.mean() * 100.0:.2f}")