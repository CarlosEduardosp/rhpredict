from pydantic import BaseModel


class Item(BaseModel):
    """ classe para inserir e validar dados de pessoa."""

    nome: str
    idade: int
    genero: int
    altura: float
    peso: float
    frequencia_alcool: int
    alimentos_alto_teor_calorico: int
    come_vegetais_nas_refeicoes: int
    quantidade_refeicoes_dia: int
    monitora_calorias_que_ingere: int
    fuma: int
    quantidade_agua_por_dia: int
    membro_familiar_com_sobre_peso: int
    frequencia_atividade_fisica: int
    tempo_que_passa_dispositivos_tecnologicos: int
    come_algo_entre_as_refeicoes: int
    qual_transporte_costuma_usar: int


