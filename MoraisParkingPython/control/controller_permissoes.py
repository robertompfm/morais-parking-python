from dao.data_permissoes import DataPermissoes
from model.area_estacionamento import AreaEstacionamento
from model.veiculo import Veiculo
from model.constants import *

class ControllerPermissoes():
    def __init__(self):
        self.data_permissoes = DataPermissoes()

    def register_permissao(self, placa, area):
        self.data_permissoes.open()
        permissao = (placa, area)
        success = self.data_permissoes.insert_permissao(permissao)
        if success:
            print("Permissao cadastrada com sucesso!")
        else:
            print("Não foi possível cadastrar a permissao")
        self.data_permissoes.close()
        return success

    def remove_permissao(self, placa, area):
        self.data_permissoes.open()
        success = self.data_permissoes.delete_permissao((placa, area))
        if success:
            print("Permisao removida com sucesso!")
        else:
            print("Não foi possivel remover a permissao ")
        self.data_permissoes.close()
        return success

    def find_permissoes_by_placa(self, placa):
        self.data_permissoes.open()
        permissoes = self.data_permissoes.query_permissoes_by_placa(placa)
        self.data_permissoes.close()
        return permissoes

    def find_permissao(self, permissao):
        self.data_permissoes.open()
        result = self.data_permissoes.query_permissao(permissao)
        self.data_permissoes.close()
        return result

# controller = ControllerPermissoes()
# permissoes = controller.find_permissoes_by_placa("CBA4321")
# for permissao in permissoes:
#     print(permissao)
# permissoes = controller.find_permissoes_by_placa("XXX0000")
# for permissao in permissoes:
#     print(permissao)

