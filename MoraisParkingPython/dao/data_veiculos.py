import sqlite3
from dao.db_constants import *
from model.Veiculo import Veiculo

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
        area = veiculo.get_area()
        t = (placa, modelo, cor, proprietario, area)
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
            proprietario = veiculo_data[3]
            area = veiculo_data[4]
            return Veiculo(placa, modelo, cor, proprietario, area)
        except sqlite3.Error as e:
            return None

    def delete_veiculo_by_placa(self, placa):
        try:
            self.c.execute(QUERY_VEICULO_BY_PLACA, (placa))
            veiculo_data = self.c.fetchone()
            if veiculo_data is None:
                return False
            self.c.execute(DELETE_VEICULO, (placa))
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

moto = Veiculo("ABC1234", "Honda", "Vermelho", "Artur")
carro = Veiculo("CBA4321", "Kombi", "Branco", "Iria")
onibus = Veiculo("XXX0000", "Mercedes Benz", "Branco", "Roberto")


data_veiculos = DataVeiculos()
data_veiculos.open()
data_veiculos.drop_veiculos_table()
data_veiculos.create_veiculos_table()
data_veiculos.insert_veiculo(moto)
data_veiculos.insert_veiculo(carro)
data_veiculos.insert_veiculo(onibus)
print(data_veiculos.query_veiculo_by_placa("ABC1234"))
data_veiculos.close()

