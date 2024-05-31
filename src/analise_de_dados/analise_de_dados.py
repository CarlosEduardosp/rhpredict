import pandas as pd
import numpy as np
from src.analise_de_dados.previsores.previsores_escalonado import Previsores_escalonado
from src.analise_de_dados.previsores.previsores2 import Previsores2
from src.analise_de_dados.previsores.previsores3 import Previsores3
from src.analise_de_dados.Chamar_algoritimo.chamar_algoritimo import chamarAlgoritimo

# Configurar pandas para comportamento futuro
pd.set_option('future.no_silent_downcasting', True)

# Ajustar a largura máxima de exibição
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# lendo o arquivo csv
df = pd.read_csv('../../dados_funcionarios.csv',
                     sep=',', encoding='utf-8')

# mostrando a tabela na tela com o print
#print(df.shape)

# mostra quantidade de linhas e colunas
print(df.shape)

# mostra os tipos dos valores dentro de cada celula.
#print(df.dtypes)

# descobrir valores que aparecem pelo menos uma vez na coluna, parametro é o nome da coluna.
valores_unicos = df['Gender'].unique()
#print(valores_unicos)

# Transformando as variáveis categóricas nominais em variáveis categóricas ordinais
# criando um dataframe
df2 = pd.DataFrame.copy(df)
print(df2.head(10))

# excluindo a a coluna CITY, por não haver necessidade.
df2.drop('City', axis=1, inplace=True)

# tranformando as variaveis
df2['Education'] = df2['Education'].replace({'Bachelors': int(0), 'Masters': int(1), 'PHD': int(2)}).astype(int)
df2['Gender'] = df2['Gender'].replace({'Male': int(0), 'Female': int(1)}).astype(int)
df2['EverBenched'] = df2['EverBenched'].replace({'No': int(0), 'Yes': int(1)}).astype(int)
#print(df2.head(10))




# alvo = variável que se pretende atingir (tem ou não doença cardíaca).
# previsores = conjunto de variáveis previsoras com as variáveis categóricas transformadas em numéricas manualmente, sem escalonar.

previsores = df2.iloc[:, 0:7].values
#print(previsores)

#print(previsores.shape)

# Alvo
alvo = df2.iloc[:, 7].values
#print(alvo)

# Analise de escalas dos atributos
#print(df2.describe())

"""
alvo = variável que se pretende atingir (tem ou não doença cardíaca).
previsores = conjunto de variáveis previsoras com as variáveis categóricas transformadas em numéricas manualmente, sem escalonar.
previsores_esc = conjunto de variáveis previsoras com as variáveis categóricas transformadas em numéricas, escalonada.
previsores2 = conjunto de variáveis previsoras com as variáveis categóricas transformadas em numéricas pelo labelencoder.
previsores2_esc = conjunto de variáveis previsoras com as variáveis categóricas transformadas em numéricas pelo labelencoder, escalonada.
previsores3 = conjunto de variáveis previsoras transformadas pelo labelencoder e onehotencoder, sem escalonar.
previsores3_esc = conjunto de variáveis previsoras transformadas pelo labelencoder e onehotencoder escalonada.
"""
print(f'Previsores: {previsores}')

previsores_escalonado = Previsores_escalonado(previsores)
print(f'Previsores escalonado: {previsores_escalonado}')

previsores2 = Previsores2(df=df)
print(f'Previsores2: {previsores2}')

previsores2_escalonado = Previsores_escalonado(previsores2)
print(f"Previsores2_escalonado: {previsores2_escalonado}")

previsores3 = Previsores3(previsores2)
# visualizando com dataframeS
previsores3df = pd.DataFrame(previsores3)
print(f'Previsores3: {previsores3df}')

previsores3_escalonado = Previsores_escalonado(previsores3)
previsores3_escdf = pd.DataFrame(previsores3_escalonado)
print(f'Previsores3_escalonado: {previsores3_escdf}')

# reunindo todos os previsores em uma lista.
todos_os_previsores = [
      {"id": "previsores", "previsores": previsores},
      {"id": "previsores_esc", "previsores": previsores_escalonado},
      {"id": "previsores2", "previsores": previsores2},
      {"id": "previsores2_esc", "previsores": previsores2_escalonado},
      {"id": "previsores3", "previsores": previsores3},
      {"id": "previsores3_esc", "previsores": previsores3_escalonado},
]

#salvando os arquivos no diretório designado.
np.savetxt('../desenvolvimento/dados_csv/previsores.csv', previsores, delimiter=',')
np.savetxt('../desenvolvimento/dados_csv/alvo.csv', alvo, delimiter=',')

# testando e avaliando com naive bayes
#chamarAlgoritimo(todos_os_previsores, alvo, codigo_algoritimo=1)

# testando e avaliando com SVM - Máquinas de Vetores de Suporte
#chamarAlgoritimo(todos_os_previsores, alvo, codigo_algoritimo=2)

# testando e avaliando com Regressão Logística
#chamarAlgoritimo(todos_os_previsores, alvo, codigo_algoritimo=3)

# testando e avaliando com KNN - aprendizagem baseada em instâncias
#chamarAlgoritimo(todos_os_previsores, alvo, codigo_algoritimo=4)

# testando e avaliando com Árvore de Decisão
#chamarAlgoritimo(todos_os_previsores, alvo, codigo_algoritimo=5)

# testando e avaliando com Random Forest
#chamarAlgoritimo(todos_os_previsores, alvo, codigo_algoritimo=6)

# testando e avaliando com XGBoost
#chamarAlgoritimo(todos_os_previsores, alvo, codigo_algoritimo=7)

# testando e avaliando com lightGbm
#chamarAlgoritimo(todos_os_previsores, alvo, codigo_algoritimo=8)

# testando e avaliando com Catboost
#chamarAlgoritimo(todos_os_previsores, alvo, codigo_algoritimo=9)
