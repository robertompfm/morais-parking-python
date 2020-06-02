import sqlite3
from dao.db_constants import *
from model.area_estacionamento import AreaEstacionamento
from model.constants import *


class DataAreaEstacionamento():
    def open(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.c = self.conn.cursor()

    def drop_area_table(self):
        try:
            self.c.execute(DROP_AREAS_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def create_areas_table(self):
        try:
            self.c.execute(CREATE_AREAS_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def insert_area(self, area):
        nome = area.get_nome()
        ocupacao = area.get_ocupacao()
        capacidade = area.get_capacidade()
        tipo = area.get_tipo()
        especial = area.is_especial()
        t = (nome, ocupacao, capacidade, tipo, especial)
        try:
            self.c.execute(INSERT_AREA, t)
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def query_area_by_nome(self, nome):
        try:
            self.c.execute(QUERY_AREA_BY_NOME, (nome,))
            area_data = self.c.fetchone()
            if area_data is not None:
                nome = area_data[0]
                ocupacao = area_data[1]
                capacidade = area_data[2]
                tipo = area_data[3]
                especial = area_data[4] == 1
                return AreaEstacionamento(nome, tipo, capacidade, especial, ocupacao)
        except sqlite3.Error:
            return None


    def query_areas_especiais(self):
        return self.query_areas(1)

    def query_areas_comuns(self):
        return self.query_areas(0)

    def query_areas(self, especial):
        try:
            self.c.execute(QUERY_SPECIAL_AREAS, (especial,))
            areas_data = self.c.fetchall()
            areas = []
            for area_data in areas_data:
                nome = area_data[0]
                ocupacao = area_data[1]
                capacidade = area_data[2]
                tipo = area_data[3]
                especial = area_data[4] == 1
                areas.append(AreaEstacionamento(nome, tipo, capacidade, especial, ocupacao))
            return areas
        except sqlite3.Error:
            return []


    def query_areas_comuns_compativeis(self, tipo):
        return self.query_areas_compativeis(0, tipo)


    def query_areas_especiais_compativeis(self, tipo):
        return self.query_areas_compativeis(1, tipo)


    def query_areas_compativeis(self, especial, tipo):
        try:
            self.c.execute(QUERY_AREAS_COMPATIVEIS, (especial, tipo))
            areas_data = self.c.fetchall()
            areas = []
            for area_data in areas_data:
                nome = area_data[0]
                ocupacao = area_data[1]
                capacidade = area_data[2]
                tipo = area_data[3]
                especial = area_data[4] == 1
                areas.append(AreaEstacionamento(nome, tipo, capacidade, especial, ocupacao))
            return areas
        except sqlite3.Error:
            return []


    def query_all_areas(self):
        try:
            self.c.execute(QUERY_ALL_AREAS)
            areas_data = self.c.fetchall()
            areas = []
            for area_data in areas_data:
                nome = area_data[0]
                ocupacao = area_data[1]
                capacidade = area_data[2]
                tipo = area_data[3]
                especial = area_data[4] == 1
                areas.append(AreaEstacionamento(nome, tipo, capacidade, especial, ocupacao))
            return areas
        except sqlite3.Error:
            return []


    def delete_area_by_nome(self, nome):
        try:
            self.c.execute(QUERY_AREA_BY_NOME, (nome,))
            area_data = self.c.fetchone()
            if area_data is None:
                return False
            if area_data[4] == 0:
                return False
            self.c.execute(DELETE_PERMISSOES_BY_AREA, (nome,))
            self.c.execute(DELETE_RESERVAS_BY_AREA, (nome,))
            self.c.execute(DELETE_AREA, (nome,))
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


# carros = AreaEstacionamento("Carros", TIPO_VEICULO[1], 30, False)
# motos = AreaEstacionamento("Motos", TIPO_VEICULO[2], 20, False)
# onibus = AreaEstacionamento("Ônibus", TIPO_VEICULO[3], 20, False)
# deficientes = AreaEstacionamento("Deficientes", TIPO_VEICULO[1], 5, True)
# vip = AreaEstacionamento("VIP", TIPO_VEICULO[1], 5, True)
#
# data_areas = DataAreaEstacionamento()
# data_areas.open()
# data_areas.drop_area_table()
# data_areas.create_areas_table()
# data_areas.insert_area(carros)
# data_areas.insert_area(motos)
# data_areas.insert_area(onibus)
# data_areas.insert_area(deficientes)
# data_areas.insert_area(vip)
# print(data_areas.query_area_by_nome("Carros"))
# print(data_areas.query_area_by_nome("Deficientes"))
# print(data_areas.query_area_by_nome("VIP"))
# data_areas.delete_area_by_nome("VIP")
# for area in data_areas.query_areas_comuns():
#     print(area)
# for area in data_areas.query_areas_especiais():
#     print(area)
# for area in data_areas.query_areas_especiais_compativeis(TIPO_VEICULO[1]):
#     print(area)
# print(data_areas.query_area_by_nome("VIP"))
# data_areas.close()