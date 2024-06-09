import requests

# URL da API
url = 'https://rhpredict-backend-github.onrender.com/inserir_dados'

dados = {
    'grau_estudo': 1,
    'ano_contratacao': 2017,
    'nivel_pagamento': 1,
    'idade': 38,
    'genero': 0,
    'ever': 1,
    'experiencia': 10
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
