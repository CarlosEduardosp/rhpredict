def Validar_dados_entrada(
        grau_de_instrucao,
        ano_de_adesao,
        nivel_de_pagamento,
        idade,
        genero,
        everbench,
        experiencia_no_dominio_atual
) -> bool:
    """ Validador de dados """
    if ano_de_adesao > 2024 or ano_de_adesao < 1970:
        return {"success": False, "data": "Ano de adesão, deve ser um valor entre '1970' e '2024'."}

    if not isinstance(idade, int):
        return {"success": False, "data": "Idade deve ser um numero inteiro."}




    return {"success": True, "data": "Tudo Ok"}
