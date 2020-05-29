from dao.data_area import DataAreaEstacionamento
from model.area_estacionamento import AreaEstacionamento

class ControllerAreaEstacionamento():
    def __init__(self):
        self.data_area = DataAreaEstacionamento()

    def register_area(self, nome, capacidade):
        self.data_area.open()
        area = AreaEstacionamento(nome, capacidade)
        success = self.data_area.insert_area(area)
        if success:
            print("Area cadastrado com sucesso!")
        else:
            print("Não foi possível cadastrar a area")
        self.data_area.close()
        return success

    def remove_area(self, nome):
        self.data_area.open()
        area = self.data_area.delete_area_by_nome(nome)
        if area:
            print("Area foi removida!")
        else:
            print("Não foi possivel remover a area ")
        self.data_area.close()
        return area

    def find_area(self, nome):
        self.data_area.open()
        area = self.data_area.query_area_by_nome(nome)
        if area is None:
            print("Area não está cadastrada")
        self.data_area.close()
        return area