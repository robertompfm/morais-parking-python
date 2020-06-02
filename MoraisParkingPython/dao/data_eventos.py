import sqlite3
from dao.db_constants import *
from model.area_estacionamento import AreaEstacionamento
from model.evento import Evento
from model.constants import *
from datetime import datetime


class DataEventos():
    def open(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.c = self.conn.cursor()

    def drop_eventos_table(self):
        try:
            self.c.execute(DROP_EVENTOS_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def create_eventos_table(self):
        try:
            self.c.execute(CREATE_EVENTOS_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def insert_evento(self, nome, inicio, fim):
        try:
            queried = self.query_evento_by_nome(nome)
            if queried is not None:
                return False
            self.c.execute(INSERT_EVENTO, (nome, inicio, fim))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def query_evento_by_nome(self, nome):
        try:
            self.c.execute(QUERY_EVENTO_BY_NAME, (nome,))
            evento_data = self.c.fetchone()
            evento = None
            if evento_data is not None:
                nome = evento_data[0]
                inicio = (datetime.strptime(evento_data[1], "%Y-%m-%d")).date()
                fim = (datetime.strptime(evento_data[2], "%Y-%m-%d")).date()
                evento = Evento(nome, inicio, fim)
            return evento
        except sqlite3.Error:
            return None

    def query_all_eventos(self):
        try:
            self.c.execute(QUERY_ALL_EVENTOS)
            eventos_data = self.c.fetchall()
            eventos = []
            for evento_data in eventos_data:
                nome = evento_data[0]
                inicio = (datetime.strptime(evento_data[1], "%Y-%m-%d")).date()
                fim = (datetime.strptime(evento_data[2], "%Y-%m-%d")).date()
                eventos.append(Evento(nome, inicio, fim))
            return eventos
        except sqlite3.Error:
            return []

    def delete_evento(self, nome):
        try:
            self.c.execute(DELETE_EVENTO, (nome,))
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def close(self):
        try:
            self.conn.close()
            return True
        except sqlite3.Error:
            return False


# data_eventos = DataEventos()
# data_eventos.open()
# data_eventos.drop_eventos_table()
# data_eventos.create_eventos_table()
# inicio = (datetime.strptime("2020-05-25", "%Y-%m-%d")).date()
# fim = (datetime.strptime("2020-06-12", "%Y-%m-%d")).date()
# data_eventos.insert_evento("INOVA", inicio, fim)
# inicio = (datetime.strptime("2020-12-10", "%Y-%m-%d")).date()
# fim = (datetime.strptime("2020-12-24", "%Y-%m-%d")).date()
# data_eventos.insert_evento("Hackathon", inicio, fim)
# print(data_eventos.query_evento_by_nome("INOVA"))
# for evento in data_eventos.query_all_eventos():
#     print(evento)
# data_eventos.delete_evento("Hackathon")
# data_eventos.insert_permissao(("CBA4321", "Deficientes"))
# data_eventos.insert_permissao(("CBA4321", "VIP"))
# for permissao in data_eventos.query_permissoes_by_placa("CBA4321"):
#     print(permissao)
# print(data_eventos.query_permissao(("CBA4321", "VIP")))
# # print(data_permissoes.delete_permissoes_by_veiculo(("CBA4321")))

# data_eventos.close()

# print((datetime.strptime("2020-05-25", "%Y-%m-%d")).date())
# print((datetime.strptime("2020-05-30", "%Y-%m-%d")).date() <= datetime.now().date())
