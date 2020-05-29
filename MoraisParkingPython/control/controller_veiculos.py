from dao.data_veiculos import DataVeiculos
from model.veiculo import Veiculo

class ControllerVeiculos():

    def __init__(self):
        self.data_veiculos = DataVeiculos()


    def register_veiculo(self, placa, modelo, cor, proprietario, nome_area):
        self.data_veiculos.open()
        veiculo = Veiculo(placa, modelo, cor, proprietario, nome_area)
        success = self.data_veiculos.insert_veiculo(veiculo)
        if success:
            print("Veículo cadastrado com sucesso!")
        else:
            print("Não foi possível cadastrar o veículo")
        self.data_veiculos.close()
        return success

    def remove_veiculo(self, placa):
        self.data_veiculos.open()
        veiculo = self.data_veiculos.delete_veiculo_by_placa(placa)
        if veiculo:
            print("Veículo foi removido")
        else:
            print("Não foi possivel remover veículo")
        self.data_veiculos.close()
        return veiculo

    def find_veiculo(self, placa):
        self.data_veiculos.open()
        veiculo = self.data_veiculos.query_veiculo_by_placa(placa)
        if veiculo is None:
            print("Veículo não cadastrado")
        self.data_veiculos.close()
        return veiculo

