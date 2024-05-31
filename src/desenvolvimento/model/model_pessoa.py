


class Pessoa:
    def __init__(self,
                 nome,
                 idade,
                 genero,
                 altura,
                 peso,
                 frequencia_alcool,
                 alimentos_alto_teor_calorico,
                 come_vegetais_nas_refeicoes,
                 quantidade_refeicoes_dia,
                 monitora_calorias_que_ingere,
                 fuma,
                 quantidade_agua_por_dia,
                 membro_familiar_com_sobre_peso,
                 frequencia_atividade_fisica,
                 tempo_que_passa_dispositivos_tecnologicos,
                 come_algo_entre_as_refeicoes,
                 qual_transporte_costuma_usar):

        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.altura = altura
        self.peso = peso
        self.frequencia_alcool = frequencia_alcool
        self.alimentos_alto_teor_calorico = alimentos_alto_teor_calorico
        self.come_vegetais_nas_refeicoes = come_vegetais_nas_refeicoes
        self.quantidade_refeicoes_dia = quantidade_refeicoes_dia
        self.monitora_calorias_que_ingere = monitora_calorias_que_ingere
        self.fuma = fuma
        self.quantidade_agua_por_dia = quantidade_agua_por_dia
        self.membro_familiar_com_sobre_peso = membro_familiar_com_sobre_peso
        self.frequencia_atividade_fisica = frequencia_atividade_fisica
        self.tempo_que_passa_dispositivos_tecnologicos = tempo_que_passa_dispositivos_tecnologicos
        self.come_algo_entre_as_refeicoes = come_algo_entre_as_refeicoes
        self.qual_transporte_costuma_usar = qual_transporte_costuma_usar


    def listar_atributos(self):

        dados = [
            self.idade,
            self.genero,
            self.altura,
            self.peso,
            self.frequencia_alcool,
            self.alimentos_alto_teor_calorico,
            self.come_vegetais_nas_refeicoes,
            self.quantidade_refeicoes_dia,
            self.monitora_calorias_que_ingere,
            self.fuma,
            self.quantidade_agua_por_dia,
            self.membro_familiar_com_sobre_peso,
            self.frequencia_atividade_fisica,
            self.tempo_que_passa_dispositivos_tecnologicos,
            self.come_algo_entre_as_refeicoes,
            self.qual_transporte_costuma_usar
        ]

        return dados

    def exibir_nome(self):

        return self.nome

    def exibir_resultado(self, resultado):

        if resultado == 0:
            return "Você está abaixo do peso ideal. Que tal consultar um nutricionista para melhorar sua alimentação?"
        elif resultado == 1:
            return "Parabéns! Você está com um peso saudável. Continue mantendo seu estilo de vida equilibrado!"
        elif resultado == 2:
            return "Você está no primeiro nível de sobrepeso. Pequenas mudanças na dieta e na atividade física podem fazer uma grande diferença!"
        elif resultado == 3:
            return "Atenção! Você está no segundo nível de sobrepeso. É uma boa ideia procurar orientação para uma vida mais saudável."
        elif resultado == 4:
            return "Você está no nível 1 de obesidade. Um plano de ação com profissionais pode ajudar a melhorar sua saúde."
        elif resultado == 5:
            return "Você está no nível 2 de obesidade. Buscar ajuda médica e ajustar seu estilo de vida pode ser muito benéfico."
        elif resultado == 6:
            return "Você está no nível 3 de obesidade. É fundamental procurar ajuda médica para garantir uma melhora na sua saúde."
        else:
            return "Resultado inválido. Por favor, verifique os dados inseridos."