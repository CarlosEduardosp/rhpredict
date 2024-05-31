


class Pessoa:
    def __init__(self,
                 grau_de_instrucao,
                 ano_de_adesao,
                 nivel_de_pagamento,
                 idade,
                 genero,
                 everbench,
                 experiencia_no_dominio_atual):

        self.grau_de_instrucao = grau_de_instrucao
        self.ano_de_adesao = ano_de_adesao
        self.nivel_de_pagamento = nivel_de_pagamento
        self.idade = idade
        self.genero = genero
        self.everbench = everbench
        self.experiencia_no_dominio_atual = experiencia_no_dominio_atual


    def listar_atributos(self):

        dados = [
            self.grau_de_instrucao,
            self.ano_de_adesao,
            self.nivel_de_pagamento,
            self.idade,
            self.genero,
            self.everbench,
            self.experiencia_no_dominio_atual
        ]

        return dados


    def exibir_resultado(self, resultado):

        if resultado == 0:
            return "Mediante aos dados apresentados, este funcionário tem alta chance de sair da empresa."
        elif resultado == 1:
            return "Mediante aos dados apresentados, este funcionário tem baixa chance de sair da empresa."
        else:
            return "Resultado inválido. Por favor, verifique os dados inseridos."