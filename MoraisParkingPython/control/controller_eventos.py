from dao.data_eventos import DataEventos
from model.Eventos import Eventos

class ControllerEventos():
    def __init__(self):
        self.data_eventos = DataEventos()

    def register_evento(self, nome_evento, data_inicial, data_final, vagas):
        self.data_eventos.open()
        evento = Eventos(nome_evento, data_inicial, data_final, vagas)
        success = self.data_eventos.insert_ocorrencia(evento)
        if success:
            print("Evento cadastrado com sucesso!")
        else:
            print("Evento não foi cadastrado")
        self.data_eventos.close()
        return success

    def remove_evento(self, nome):
        self.data_eventos.open()
        evento = self.data_eventos.delete_evento_by_nome(nome)
        if evento:
            print("Evento foi removido!")
        else:
            print("Não foi possivel remover o evento ")
        self.data_eventos.close()
        return evento

    def find_evento(self, nome):
        self.data_eventos.open()
        evento = self.data_eventos.query_evento_by_nome(nome)
        if evento is None:
            print("Evento não está cadastrado")
        self.data_eventos.close()
        return evento