import sqlite3
from dao.db_constants import *
from model.Ocorrencias import Ocorrencias


class DataOcorrencia():
    def open(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.c = self.conn.cursor()

    def drop_ocorrencia_table(self):
        try:
            self.c.execute(DROP_OCORRENCIA_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def create_ocorrencia_table(self):
        try:
            self.c.execute(CREATE_OCORRENCIA_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def insert_ocorrencia(self, ocorrencia):
        tipo = ocorrencia.get_tipo()
        placa = ocorrencia.get_placa()
        quantidade_veiculos = ocorrencia.get_quantidade_veiculos()
        data = ocorrencia.get_data()
        hora = ocorrencia.get_hora()
        descricao = ocorrencia.get_descricao()
        t = (tipo, placa, quantidade_veiculos, data, hora, descricao)

        try:
            self.c.execute(INSERT_OCORRENCIA, t)
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def query_ocorrencia_by_tipo(self, tipo):
        try:
            self.c.execute(QUERY_OCORRENCIA_BY_TIPO, tipo)
            ocorrencia_data = self.c.fetchone()
            if ocorrencia_data is None:
                tipo = ocorrencia_data[0]
                placa = ocorrencia_data[1]
                quantidade_veiculos = ocorrencia_data[2]
                data = ocorrencia_data[3]
                hora = ocorrencia_data[4]
                descricao = ocorrencia_data[5]
                return Ocorrencias(tipo, placa, quantidade_veiculos, data, hora, descricao)
        except sqlite3.Error:
            return None

    def close(self):
        try:
            self.conn.close()
            return True
        except sqlite3.Error:
            return False


ocorrencia1 = Ocorrencias("Furto", "ABC1234", "1", "01/06/2020", "10:29", "Carro roubado")

data_ocorrencia = DataOcorrencia()
data_ocorrencia.open()
data_ocorrencia.drop_ocorrencia_table()
data_ocorrencia.create_ocorrencia_table()
data_ocorrencia.insert_ocorrencia(ocorrencia1)


