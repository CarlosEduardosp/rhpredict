import requests

# URL da API
url = 'https://rhpredict-github-backend.onrender.com/inserir_dados'

dados = {
    "grau_de_instrucao": 0,
    "ano_de_adesao": 0,
    "nivel_de_pagamento": 0,
    "idade": 0,
    "genero": 0,
    "everbench": 0,
    "experiencia_no_dominio_atual": 0
}


try:
    # Fazendo a requisição POST
    response = requests.post(url, json=dados)
    response.raise_for_status()  # Isso lançará um erro para códigos de status 4xx/5xx

    # Convertendo a resposta para JSON
    data = response.json()

    print(data)

except requests.exceptions.HTTPError as errh:
    print(f"Http Error: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Error Connecting: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
    print(f"OOps: Something Else {err}")
