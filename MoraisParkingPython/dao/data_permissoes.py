import sqlite3
from dao.db_constants import *
from model.area_estacionamento import AreaEstacionamento
from model.constants import *


class DataPermissoes():
    def open(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.c = self.conn.cursor()

    def drop_permissoes_table(self):
        try:
            self.c.execute(DROP_PERMISSOES_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def create_permissoes_table(self):
        try:
            self.c.execute(CREATE_PERMISSOES_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def insert_permissao(self, permissao):
        try:
            queried = self.query_permissao(permissao)
            if queried is None:
                self.c.execute(INSERT_PERMISSAO, permissao)
                self.conn.commit()
                return True
            return False
        except sqlite3.IntegrityError:
            return False

    def query_permissoes_by_placa(self, placa):
        try:
            self.c.execute(QUERY_PERMISSOES_BY_VEICULO, (placa,))
            permissoes_data = self.c.fetchall()
            permissoes = []
            for permissao_data in permissoes_data:
                permissao = (permissao_data[0], permissao_data[1])
                permissoes.append(permissao)
            return permissoes
        except sqlite3.Error:
            return None

    def query_permissao(self, permissao):
        try:
            self.c.execute(QUERY_PERMISSAO, permissao)
            permissao = self.c.fetchone()
            return permissao
        except sqlite3.Error:
            return None

    def delete_permissoes_by_veiculo(self, placa):
        try:
            self.c.execute(DELETE_PERMISSOES_BY_VEICULO, (placa,))
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def delete_permissoes_by_area(self, area):
        try:
            self.c.execute(DELETE_PERMISSOES_BY_AREA, (area,))
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def delete_permissao(self, permissao):
        try:
            self.c.execute(DELETE_PERMISSAO, permissao)
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


# data_permissoes = DataPermissoes()
# data_permissoes.open()
# data_permissoes.drop_permissoes_table()
# data_permissoes.create_permissoes_table()
# data_permissoes.insert_permissao(("CBA4321", "Deficientes"))
# data_permissoes.insert_permissao(("CBA4321", "VIP"))
# for permissao in data_permissoes.query_permissoes_by_placa("CBA4321"):
#     print(permissao)
# print(data_permissoes.query_permissao(("CBA4321", "VIP")))
# # print(data_permissoes.delete_permissoes_by_veiculo(("CBA4321")))
#
# data_permissoes.close()