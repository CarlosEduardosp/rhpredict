from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import KFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from src.analise_de_dados.interfaces.InterfaceAlgoritimo.interfaceAlgoritimo import AlgoritimoInterface
from sklearn.tree import DecisionTreeClassifier
from catboost import CatBoostClassifier


class AlgoritimoCatBoost(AlgoritimoInterface):

    def avaliar_e_validacao_cruzada(self, todos_os_previsores: list, alvo: list):
        self.todos_os_previsores = todos_os_previsores
        self.alvo = alvo

        print('----------------------------------------------')
        print('Testando e Avaliando CatBoost: ')
        print('----------------------------------------------')

        # dados de treino de todos os previsores de uma vez.
        for i in self.todos_os_previsores:
            print(f'Teste com {i['id']}')

            dados_treino_e_teste = self._separando_dados_para_treino_e_teste(i['previsores'], alvo)
            # print(dados_treino_e_teste)

            # aplicando o algoritimo XGboost.
            response = self._treinando_e_testando(dados_treino_e_teste)

            # validação cruzada

            # Separando os dados em folds
            kfold = KFold(n_splits=2, shuffle=True, random_state=5)

            # Criando o modelo
            modelo = make_pipeline(
                StandardScaler(),
                CatBoostClassifier(task_type='CPU', iterations=100, learning_rate=0.1, depth=8, random_state=5,
                                   eval_metric="Accuracy")
            )
            resultado = cross_val_score(modelo, i['previsores'], alvo, cv=kfold)

            # Usamos a média e o desvio padrão
            print(f"Validação Cruzada, Acurácia Média: {resultado.mean() * 100.0:.2f}")


    def _treinando_e_testando(self, dados_treino_e_teste: list):
        x_treino = dados_treino_e_teste['x_treino']
        y_treino = dados_treino_e_teste['y_treino']
        x_teste = dados_treino_e_teste['x_teste']
        y_teste = dados_treino_e_teste['y_teste']

        # treino do algoritimo
        arvore = DecisionTreeClassifier(criterion='entropy', random_state=5, max_depth=3)
        arvore.fit(x_treino, y_treino)

        # avaliação do algoritimo dados de teste.
        previsores_arvore = arvore.predict(x_teste)
        # print('teste com naive bayes', previsores_arvore)
        # print('dados de y teste', y_teste)

        # verificando a acurácia.
        acuracia_teste = accuracy_score(y_teste, previsores_arvore)
        print(f'acurácia dados de teste é de: {acuracia_teste * 100:.2f}%')

        # matrix de confusão
        matriz = confusion_matrix(y_teste, previsores_arvore)
        # print('matriz de confusão', matriz)

        # avaliação do algoritimo dados de treino.
        previsores_naive = arvore.predict(x_treino)
        # print('teste com naive bayes', previsores_naive)
        # print('dados de x treino', x_treino)

        # verificando a acurácia.
        acuracia_treino = accuracy_score(y_treino, previsores_naive)
        print(f'acurácia dados de treino é de: {acuracia_treino * 100:.2f}%')


    def _separando_dados_para_treino_e_teste(self, previsores, alvo):
        """
            :param previsores: dados para treino e teste.
            :param alvo: objetivo do treino e teste.
            :return: dados de treino e dados de teste.
            """

        x_treino, x_teste, y_treino, y_teste = train_test_split(previsores, alvo,
                                                                test_size=0.3, random_state=0)

        return {"x_treino": x_treino, "x_teste": x_teste, "y_treino": y_treino, "y_teste": y_teste}
