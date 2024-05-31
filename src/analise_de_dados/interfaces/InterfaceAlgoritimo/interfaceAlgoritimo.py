from abc import ABC, abstractmethod


class AlgoritimoInterface(ABC):

    @abstractmethod
    def avaliar_e_validacao_cruzada(self, todos_os_previsores: list, alvo: list):
        pass

    @abstractmethod
    def _treinando_e_testando(self, dados_treino_e_teste: list):
        pass

    @abstractmethod
    def _separando_dados_para_treino_e_teste(self, previsores, alvo):
        pass
