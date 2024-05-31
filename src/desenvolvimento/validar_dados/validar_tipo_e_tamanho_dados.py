def Validar_dados_entrada(
        nome: str,
        idade: int,
        genero: int,
        altura: float,
        peso: float,
        frequencia_alcool: int,
        alimentos_alto_teor_calorico: int,
        come_vegetais_nas_refeicoes: int,
        quantidade_refeicoes_dia: int,
        monitora_calorias_que_ingere: int,
        fuma: int,
        quantidade_agua_por_dia: int,
        membro_familiar_com_sobre_peso: int,
        frequencia_atividade_fisica: int,
        tempo_que_passa_dispositivos_tecnologicos: int,
        come_algo_entre_as_refeicoes: int,
        qual_transporte_costuma_usar: int
) -> bool:
    """ Validador de dados """

    if not isinstance(nome, str):
        return {"success": False, "data": "Nome deve ser uma String"}

    if len(nome) > 40:
        return {"success": False, "data": "Nome deve ser menor que 40 caracteres"}

    if idade > 130 or idade < 0:
        return {"success": False, "data": "Idade deve estar entre 0 e 130 anos."}

    if genero > 1 or alimentos_alto_teor_calorico > 1 or fuma > 1 or monitora_calorias_que_ingere > 1 or membro_familiar_com_sobre_peso > 1 or genero < 0 or alimentos_alto_teor_calorico < 0 or fuma < 0 or monitora_calorias_que_ingere < 0 or membro_familiar_com_sobre_peso < 0:
        return {"success": False, "data": "Valores Binários precisam ser entre 0 e 1."}

    if not isinstance(altura, float) or altura > 2.5 or altura < 0:
        return {"success": False, "data": "Altura deve ser um Numero válido entre 0 e 2.5m."}

    if not isinstance(peso, float):
        return {"success": False, "data": "Peso precisa ser um numero válido."}

    return {"success": True, "data": "Tudo Ok"}
