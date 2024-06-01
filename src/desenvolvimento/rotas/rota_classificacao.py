from src.desenvolvimento.model.model_pessoa import Pessoa
from src.desenvolvimento.Algoritimo_escolhido.Rodando_Algoritimo_escolhido import rodar_Algoritimo_escolhido
from fastapi import APIRouter
from src.desenvolvimento.validar_dados.inserir_validar import Item
from src.desenvolvimento.validar_dados.validar_tipo_e_tamanho_dados import Validar_dados_entrada
router = APIRouter()


@router.post('/inserir_dados')
def Inserir_dados(pessoa: Item):
    """
    :return: Inserir dados para análise.
    """

    response = Validar_dados_entrada(grau_de_instrucao=pessoa.grau_de_instrucao,
                                     ano_de_adesao=pessoa.ano_de_adesao,
                                     nivel_de_pagamento=pessoa.nivel_de_pagamento,
                                     idade=pessoa.idade,
                                     genero=pessoa.genero,
                                     everbench=pessoa.everbench,
                                     experiencia_no_dominio_atual=pessoa.experiencia_no_dominio_atual)

    if response['success']:


        dados = Pessoa(
            grau_de_instrucao=pessoa.grau_de_instrucao,
            ano_de_adesao=pessoa.ano_de_adesao,
            nivel_de_pagamento=pessoa.nivel_de_pagamento,
            idade=pessoa.idade,
            genero=pessoa.genero,
            everbench=pessoa.everbench,
            experiencia_no_dominio_atual=pessoa.experiencia_no_dominio_atual
        )

        resultado = rodar_Algoritimo_escolhido(dados)

        return {"success": True, "message": f'Olá, {dados.exibir_resultado(resultado)}'}

    return response
