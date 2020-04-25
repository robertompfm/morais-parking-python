from model.area_estacionamento import AreaEstacionamento
from model.proprietario import Proprietario
from model.veiculo import Veiculo

class Estacionamento():

    # CONSTRUCTOR
    def __init__(self, capacidade):
        self.prop_cadastrados = list()
        self.veiculos_cadastrados =list()
        self.areas_especiais = list()
        self.area_comum = AreaEstacionamento("Comum", capacidade)
        self.capacidade_maxima = capacidade

    # FIND METHODS
    def identificar_area(self, nome):
        for area in self.areas_especiais:
            if area.get_nome().upper() == nome.upper():
                return area
        return None

    def identificar_proprietario(self, nome):
        for proprietario in self.prop_cadastrados:
            if proprietario.get_nome().upper() == nome.upper():
                return proprietario
        return None

    def identificar_veiculo(self, placa):
        for veiculo in self.veiculos_cadastrados:
            if veiculo.get_placa().upper() == placa.upper():
                return veiculo
        return None

    # REGISTER METHODS
    def cadastrar_proprietario(self, nome, matricula, curso):
        proprietario = self.identificar_proprietario(nome)
        if proprietario is None:
            proprietario = Proprietario(nome, matricula, curso)
            self.prop_cadastrados.append(proprietario)
            return True
        return False

    def cadastrar_area(self, nome, capacidade):
        capacidade = capacidade if capacidade > 0 else 1
        vagas_restantes = self.area_comum.get_capacidade() - capacidade
        area = self.identificar_area(nome)
        if area is None and vagas_restantes >= 0:
            area = AreaEstacionamento(nome, capacidade)
            self.areas_especiais.append(area)
            self.area_comum.set_capacidade(vagas_restantes)
            return True
        return False

    def cadastrar_veiculo(self, nome_prop, matricula, curso, placa, modelo, cor, nome_area):
        veiculo = self.identificar_veiculo(placa)
        area = self.identificar_area(nome_area)
        if area is None and self.area_comum.get_nome() != nome_area:
            return False
        if veiculo is None:
            self.cadastrar_proprietario(nome_prop, matricula, curso)
            proprietario = self.identificar_proprietario(nome_prop)
            veiculo = Veiculo(placa, modelo, cor, proprietario, nome_area)
            self.veiculos_cadastrados.append(veiculo)
            return True
        return False

    # REMOVE METHODS
    def excluir_proprietario(self, nome):
        proprietario = self.identificar_proprietario(nome)
        if proprietario is not None:
            self.prop_cadastrados.remove(proprietario)
            return True
        return False

    def excluir_area(self, nome):
        area = self.identificar_area(nome)
        if area is not None:
            self.areas_especiais.remove(area)
            self.area_comum.set_capacidade(self.area_comum.get_capacidade() + area.get_capacidade())
            return True
        return False

    def excluir_veiculo(self, placa):
        veiculo = self.identificar_veiculo(placa)
        if veiculo is not None:
            self.veiculos_cadastrados.remove(veiculo)
            return True
        return False

    # MONITORING METHODS
    def autorizar_entrada(self, placa, modelo, cor):
        veiculo = self.identificar_veiculo(placa)
        if veiculo is None:
            veiculo = Veiculo(placa, modelo, cor)
        nome_area = veiculo.get_area()
        area = self.identificar_area(nome_area)
        if area is not None:
            if area.get_taxa_ocupacao() < 1:
                return area.adicionar_veiculo(veiculo)
            elif veiculo not in area.get_veiculos():
                return self.area_comum.adicionar_veiculo(veiculo)
            else:
                return False
        else:
            return self.area_comum.adicionar_veiculo(veiculo)

    def autorizar_saida(self, placa, modelo, cor):
        veiculo = self.identificar_veiculo(placa)
        if veiculo is None:
            veiculo = Veiculo(placa, modelo, cor)
        if self.area_comum.remover_veiculo(veiculo):
            return True
        for area in self.areas_especiais:
            if area.remover_veiculo(veiculo):
                return True
        return False

    # REPORT METHOD
    def get_status(self):
        status = "MORAIS PARKING STATUS\n\n"
        status += str(self.area_comum) + "\n"
        ocupacao = self.area_comum.get_ocupacao()
        for area in self.areas_especiais:
            status += str(area) + "\n"
            ocupacao += area.get_ocupacao()
        status += "\n"
        tx_ocupacao = ocupacao / self.capacidade_maxima
        status += "Ocupacao total: {0} / {1} ({2:.2f}%)".format(
            ocupacao, self.capacidade_maxima, (100 * ocupacao / self.capacidade_maxima)
        )
        return status

    # GETTERS AND SETTERS
    def get_prop_cadastrados(self):
        return self.prop_cadastrados

    def set_prop_cadastrados(self, prop_cadastrados):
        self.prop_cadastrados = prop_cadastrados

    def get_veiculos_cadastrados(self):
        return self.veiculos_cadastrados

    def set_veiculos_cadastrados(self, veiculos_cadastrados):
        self.veiculos_cadastrados = veiculos_cadastrados

    def get_areas_especiais(self):
        return self.areas_especiais

    def set_areas_especiais(self, areas_especiais):
        self.areas_especiais = areas_especiais

    def get_area_comum(self):
        return self.area_comum

    def set_area_comum(self, area_comum):
        self.area_comum = area_comum

    def get_capacidade_maxima(self):
        return self.capacidade_maxima

    def set_capacidade_maxima(self, capacidade_maxima):
        self.capacidade_maxima = capacidade_maxima


















