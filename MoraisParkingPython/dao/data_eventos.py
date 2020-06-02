import sqlite3
from dao.db_constants import *
from model.Eventos import Eventos

class DataEventos():
    def open(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.c = self.conn.cursor()

    def drop_eventos_table(self):
        try:
            self.c.execute(DROP_EVENTO_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def create_eventos_table(self):
        try:
            self.c.execute(CREATE_EVENTO_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def insert_ocorrencia(self, evento):
        nome_evento = evento.get_nome_evento()
        data_inicial = evento.get_data_inicial()
        data_final = evento.get_data_final()
        vagas = evento.get_vagas()
        t = Eventos(nome_evento, data_inicial, data_final, vagas)
        try:
            self.c.execute(INSERT_EVENTO, t)
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def delete_evento_by_nome(self, nome):
        try:
            self.c.execute(QUERY_EVENTO_BY_NOME, (nome))
            evento_data = self.c.fetchone()
            if evento_data is None:
                return False
            self.c.execute(DELETE_EVENTO, (nome))
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def query_evento_by_nome(self, nome):
        try:
            self.c.execute(QUERY_EVENTO_BY_NOME, nome)
            evento_data = self.c.fetchone()
            if evento_data is None:
                nome_evento = evento_data[0]
                data_inicial = evento_data[1]
                data_final = evento_data[2]
                vagas = evento_data[3]
                return Eventos(nome_evento, data_inicial, data_final, vagas)
        except sqlite3.Error:
            return None

    def close(self):
        try:
            self.conn.close()
            return True
        except sqlite3.Error:
            return False


evento1 = Eventos("Inova", "01/06/2020", "05/06/2020", "100")

data_evento = DataEventos()
data_evento.open()
data_evento.drop_eventos_table()
data_evento.create_eventos_table()
data_evento.insert_ocorrencia(evento1)
print(data_evento.query_evento_by_nome("Inova"))