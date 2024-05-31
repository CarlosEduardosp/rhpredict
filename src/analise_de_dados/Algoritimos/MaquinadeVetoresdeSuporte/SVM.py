from sklearn.metrics import accuracy_score, confusion_matrix
from src.analise_de_dados.treino_e_teste.treino_e_teste import TreinoTeste
from sklearn.model_selection import KFold, cross_val_score
from sklearn.svm import SVC


def SVM(dados_treino_e_teste: list):

    x_treino = dados_treino_e_teste['x_treino']
    y_treino = dados_treino_e_teste['y_treino']
    x_teste = dados_treino_e_teste['x_teste']
    y_teste = dados_treino_e_teste['y_teste']

    # treino do algoritimo
    svm = SVC(kernel='rbf', random_state=1, C=2)
    svm.fit(x_treino, y_treino)

    # avaliação do algoritimo dados de teste.
    previsoes_svm = svm.predict(x_teste)
    # print('teste com SVM', previsores_svm)
    # print('dados de y teste', y_teste)

    # verificando a acurácia.
    acuracia_teste = accuracy_score(y_teste, previsoes_svm)
    print(f'acurácia dados de teste é de: {accuracy_score(y_teste, previsoes_svm) * 100.0:.2f}%')

    # matrix de confusão
    matriz = confusion_matrix(y_teste, previsoes_svm)
    # print('matriz de confusão', matriz)

    # avaliação do algoritimo dados de treino.
    previsores_naive = svm.predict(x_treino)
    # print('teste com naive bayes', previsores_naive)
    # print('dados de x treino', x_treino)

    # verificando a acurácia.
    acuracia_treino = accuracy_score(y_treino, previsores_naive)
    print(f'acurácia dados de treino é de: {acuracia_treino * 100:.2f}%')


def avaliarSvm(todos_os_previsores: list, alvo: list, ):

    print('----------------------------------------------')
    print('Testando e Avaliando SVM: ')
    print('----------------------------------------------')

    # dados de treino de todos os previsores de uma vez.
    for i in todos_os_previsores:
        print(f'Teste com {i['id']}')

        dados_treino_e_teste = TreinoTeste(i['previsores'], alvo)
        # print(dados_treino_e_teste)

        # aplicando o algoritimo naive bayes.
        response = SVM(dados_treino_e_teste)

        # validação cruzada

        # Separando os dados em folds
        kfold = KFold(n_splits=30, shuffle=True, random_state=5)

        # Criando o modelo
        modelo = SVC(kernel='rbf', random_state=10, C=2)
        resultado = cross_val_score(modelo, i['previsores'], alvo, cv=kfold)

        # Usamos a média e o desvio padrão
        print(f"Validação Cruzada, Acurácia Média: {resultado.mean() * 100.0}")
