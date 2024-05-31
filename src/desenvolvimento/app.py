from fastapi import FastAPI
from src.desenvolvimento.rotas import inicio, rota_classificacao
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(inicio.router, tags=["Mensagem Inicial da api."])
app.include_router(rota_classificacao.router, tags=["Inserir dados para análise."])


# Lista de origens permitidas
allowed_origins = [
    "http://www.icnvararuama.com.br",
    "https://www.icnvararuama.com.br",
    "http://170.231.112.194",
    "http://icnvararuama.netlify.app",
    "https://icnvararuama.netlify.app",
    "http://2600:1f1e:c3c:f302::c8",
    "http://2600:1f1e:c3c:f301::c8",
    "http://52.67.97.86",
    "http://177.71.195.255",
    "http://170.231.112.205"
]

# Configurar CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Substitua pelo domínio do seu aplicativo, * para todos os dominios
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PUT"],  # Você pode especificar métodos permitidos, como ["GET", "POST"]
    allow_headers=["Authorization"],  # Você pode especificar cabeçalhos permitidos, como ["Authorization"]
)


