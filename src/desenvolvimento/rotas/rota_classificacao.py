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

    response = Validar_dados_entrada(nome=pessoa.nome,
                                     idade=pessoa.idade,
                                     genero=pessoa.genero,
                                     altura=pessoa.altura,
                                     peso=pessoa.peso,
                                     frequencia_alcool=pessoa.frequencia_alcool,
                                     alimentos_alto_teor_calorico=pessoa.alimentos_alto_teor_calorico,
                                     come_vegetais_nas_refeicoes=pessoa.come_vegetais_nas_refeicoes,
                                     quantidade_refeicoes_dia=pessoa.quantidade_refeicoes_dia,
                                     monitora_calorias_que_ingere=pessoa.monitora_calorias_que_ingere,
                                     fuma=pessoa.fuma,
                                     quantidade_agua_por_dia=pessoa.quantidade_agua_por_dia,
                                     membro_familiar_com_sobre_peso=pessoa.membro_familiar_com_sobre_peso,
                                     frequencia_atividade_fisica=pessoa.frequencia_atividade_fisica,
                                     tempo_que_passa_dispositivos_tecnologicos=pessoa.tempo_que_passa_dispositivos_tecnologicos,
                                     come_algo_entre_as_refeicoes=pessoa.come_algo_entre_as_refeicoes,
                                     qual_transporte_costuma_usar=pessoa.qual_transporte_costuma_usar)

    if response['success']:


        dados = Pessoa(
            nome=pessoa.nome,
            idade=pessoa.idade,
            genero=pessoa.genero,
            altura=pessoa.altura,
            peso=pessoa.peso,
            frequencia_alcool=pessoa.frequencia_alcool,
            alimentos_alto_teor_calorico=pessoa.alimentos_alto_teor_calorico,
            come_vegetais_nas_refeicoes=pessoa.come_vegetais_nas_refeicoes,
            quantidade_refeicoes_dia=pessoa.quantidade_refeicoes_dia,
            monitora_calorias_que_ingere=pessoa.monitora_calorias_que_ingere,
            fuma=pessoa.fuma,
            quantidade_agua_por_dia=pessoa.quantidade_agua_por_dia,
            membro_familiar_com_sobre_peso=pessoa.membro_familiar_com_sobre_peso,
            frequencia_atividade_fisica=pessoa.frequencia_atividade_fisica,
            tempo_que_passa_dispositivos_tecnologicos=pessoa.tempo_que_passa_dispositivos_tecnologicos,
            come_algo_entre_as_refeicoes=pessoa.come_algo_entre_as_refeicoes,
            qual_transporte_costuma_usar=pessoa.qual_transporte_costuma_usar
        )

        resultado = rodar_Algoritimo_escolhido(dados)

        return {"success": True, "message": f'Olá {dados.exibir_nome()}, {dados.exibir_resultado(resultado)}'}

    return response
