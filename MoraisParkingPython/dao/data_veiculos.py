import sqlite3
from dao.db_constants import *
from model.veiculo import Veiculo
from model.proprietario import Proprietario
from model.constants import *

class DataVeiculos():
    def open(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.c = self.conn.cursor()

    def drop_veiculos_table(self):
        try:
            self.c.execute(DROP_VEICULOS_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def create_veiculos_table(self):
        try:
            self.c.execute(CREATE_VEICULOS_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def insert_veiculo(self, veiculo):
        placa = veiculo.get_placa()
        modelo = veiculo.get_modelo()
        cor = veiculo.get_cor()
        proprietario = veiculo.get_proprietario()
        proprietario_nome = proprietario.get_nome()
        tipo = veiculo.get_tipo()
        t = (placa, modelo, cor, proprietario_nome, tipo)
        try:
            self.c.execute(INSERT_VEICULO, t)
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def query_veiculo_by_placa(self, placa):
        try:
            self.c.execute(QUERY_VEICULO_BY_PLACA, (placa,))
            veiculo_data = self.c.fetchone()
            if veiculo_data is None:
                return None
            placa = veiculo_data[0]
            modelo = veiculo_data[1]
            cor = veiculo_data[2]
            proprietario_nome = veiculo_data[3]
            area = veiculo_data[4]
            self.c.execute(QUERY_PROPRIETARIO_BY_NOME, (proprietario_nome,))
            proprietario_info = self.c.fetchone()
            proprietario = Proprietario(
                proprietario_info[0],
                proprietario_info[1],
                proprietario_info[2]
            )
            return Veiculo(placa, modelo, cor, proprietario, area)
        except sqlite3.Error as e:
            return None

    def delete_veiculo_by_placa(self, placa):
        try:
            self.c.execute(QUERY_VEICULO_BY_PLACA, (placa,))
            veiculo_data = self.c.fetchone()
            if veiculo_data is None:
                return False
            self.c.execute(DELETE_VEICULO, (placa,))
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


# arthur = Proprietario("Arthur", "20192007000", "Sistemas para Internet")
# larissa = Proprietario("Arthur", "20192007001", "Sistemas para Internet")
# roberto = Proprietario("Roberto", "20192007002", "Sistemas para Internet")
# iria = Proprietario("Iria", "20192007003", "Sistemas para Internet")
#
# moto = Veiculo("ABC1234", "Honda", "Vermelho", arthur, TIPO_VEICULO[2])
# carro = Veiculo("CBA4321", "Kombi", "Branco", iria, TIPO_VEICULO[1])
# onibus = Veiculo("XXX0000", "Mercedes Benz", "Branco", roberto, TIPO_VEICULO[3])
#
#
# data_veiculos = DataVeiculos()
# data_veiculos.open()
# data_veiculos.drop_veiculos_table()
# data_veiculos.create_veiculos_table()
# data_veiculos.insert_veiculo(moto)
# data_veiculos.insert_veiculo(carro)
# data_veiculos.insert_veiculo(onibus)
# print(data_veiculos.query_veiculo_by_placa("ABC1234"))
# # data_veiculos.delete_veiculo_by_placa("ABC1234")
# print(data_veiculos.query_veiculo_by_placa("ABC1234"))
# data_veiculos.close()

