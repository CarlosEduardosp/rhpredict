from fastapi import APIRouter
from fastapi.responses import StreamingResponse

router = APIRouter()


@router.get('/')
def inicio():
    """
    :return: Mensagem de inicio na api.
    """

    response = {
        "Success": 200,
        "Message": "API para análisar a permanência de uma pessoa em uma empresa, utilizando tecnicas de machine learning.",
        "Info": "Use /docs para acessar a documentação no Swagger ",
        "Dev": "Carlos Eduardo dos S. Padilha",
        "Algoritimo Utilizado": "SVM - Maquina de Vetores de Suporte "
    }

    return response

