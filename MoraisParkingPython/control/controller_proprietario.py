from dao.data_proprietarios import DataProprietarios
from model.Proprietario import Proprietario


class ControllerProprietarios():

    def __init__(self):
        self.data_proprietario = DataProprietarios()

    def register_proprietario(self, nome, matricula, curso):
        self.data_proprietario.open()
        proprietario = Proprietario(nome, matricula, curso)
        success = self.data_proprietario.insert_proprietarios(proprietario)
        if success:
            print("Prprietario cadastrado com sucesso!")
        else:
            print("Não foi possível cadastrar o proprietario")
        self.data_proprietario.close()
        return success

    def remove_proprietario(self, nome):
        self.data_proprietario.open()
        proprietario = self.data_proprietario.delete_proprietario_by_nome(nome)
        if proprietario:
            print("Proprietario foi removido!")
        else:
            print("Não foi possivel remover o veiculo")
        self.data_proprietario.close()
        return proprietario

    def find_proprietarios(self, nome):
        self.data_proprietario.open()
        proprietario = self.data_proprietario.query_proprietarios_by_nome(nome)
        if proprietario is None:
            print("Proprietario não cadastrado")
        self.data_proprietario.close()
        return proprietario
