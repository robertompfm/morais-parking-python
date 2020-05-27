import sqlite3
from dao.db_constants import *
from model.Proprietario import Proprietario


class DataProprietarios():
    def open(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.c = self.conn.cursor()

    def drop_proprietarios_table(self):
        try:
            self.c.execute(DROP_PROPRIETARIOS_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def create_proprietarios_table(self):
        try:
            self.c.execute(CREATE_PROPRIETARIOS_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def insert_proprietarios(self, proprietario):
        nome = proprietario.get_nome()
        matricula = proprietario.get_matricula()
        curso = proprietario.get_curso()
        t = (nome, matricula, curso)
        try:
            self.c.execute(INSERT_PROPRIETARIOS, t)
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def query_proprietarios_by_nome(self, nome):
        try:
            self.c.execute(QUERY_PROPRIETARIOS_BY_NOME, (nome,))
            proprietario_data = self.c.fetchone()
            if proprietario_data is None:
                nome = proprietario_data[0]
                matricula = proprietario_data[1]
                curso = proprietario_data[2]
                return Proprietario(nome, matricula, curso)
        except sqlite3.Error:
            return None

    def delete_proprietario_by_nome(self, nome):
        try:
            self.c.execute(QUERY_PROPRIETARIOS_BY_NOME, (nome,))
            proprietario_data = self.c.fetchone()
            if proprietario_data in None:
                return False
            self.c.execute(DELETE_PROPRIETARIOS, (nome,))
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



'''artur = Proprietario("Artur", "20192007000", "Sistemas para Internet")
roberto = Proprietario("Roberto", "20192007001", "Sistemas para Internet")
iria = Proprietario("Iria", "20192007002", "Sistemas para Internet")


data_proprietarios = DataProprietarios()
data_proprietarios.open()
data_proprietarios.drop_proprietarios_table()
data_proprietarios.create_proprietarios_table()
data_proprietarios.insert_proprietarios(artur)
data_proprietarios.insert_proprietarios(roberto)
data_proprietarios.insert_proprietarios(iria)
print(data_proprietarios.query_proprietarios_by_nome('Artur'))
data_proprietarios.close()'''