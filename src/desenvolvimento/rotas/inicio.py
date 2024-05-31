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
        "Message": "API para análise de peso de indivíduos através de machine learning.",
        "Info": "Use /docs para acessar a documentação no Swagger ",
        "Dev": "Carlos Eduardo dos S. Padilha",
        "Algoritimo Utilizado": "Regressão Logistica"
    }

    return response

