import sqlite3
from dao.db_constants import *
from model.AreaEstacionamento import AreaEstacionamento

class DataAreaEstacionamento():
    def open(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.c = self.conn.cursor()

    def drop_area_table(self):
        try:
            self.c.execute(DROP_AREA_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def create_area_table(self):
        try:
            self.c.execute(CREATE_AREA_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def insert_area(self, area):
        nome = area.get_nome()
        capacidade = area.get_capacidade()
        t = (nome, capacidade)
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
            if area_data is None:
                nome = area_data[0]
                capacidade = area_data[1]
                return AreaEstacionamento(nome, capacidade)
        except sqlite3.Error:
            return None

    def delete_area_by_nome(self, nome):
        try:
            self.c.execute(QUERY_AREA_BY_NOME, (nome,))
            area_data = self.c.fetchone()
            if area_data in None:
                return False
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

'''area1 = AreaEstacionamento("Carros", "30")
area2 = AreaEstacionamento("Ônibus", "20")
area3 = AreaEstacionamento("Motos", "20")

data_area = DataAreaEstacionamento()
data_area.open()
data_area.drop_area_table()
data_area.create_area_table()
data_area.insert_area(area1)
data_area.insert_area(area2)
data_area.insert_area(area3)
print(data_area.query_area_by_nome("Carros"))'''