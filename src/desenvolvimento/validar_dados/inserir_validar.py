from pydantic import BaseModel


class Item(BaseModel):
    """ classe para inserir e validar dados de pessoa."""

    grau_de_instrucao: int
    ano_de_adesao: int
    nivel_de_pagamento: int
    idade: int
    genero: int
    everbench: int
    experiencia_no_dominio_atual: int


