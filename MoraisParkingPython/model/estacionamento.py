from model.area_estacionamento import AreaEstacionamento
from model.proprietario import Proprietario
from model.veiculo import Veiculo
from model.usuario import Usuario
from model.ocorrencias import Ocorrencias
from model.eventos import Eventos

class Estacionamento():

    # CONSTRUCTOR
    def __init__(self, capacidade):
        self.prop_cadastrados = list()
        self.veiculos_cadastrados = list()
        self.areas_especiais = list()
        self.cadastrar_usuario = list()
        self.cadastrar_ocorrencia = list()
        self.cadastrar_eventos = list()
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

    def identificar_ocorrencia(self, tipo):
        for ocorrencia in self.cadastrar_ocorrencia:
            if tipo == ocorrencia.get_tipo():
                return ocorrencia
        return None

    def identificar_evento(self, nome_evento):
        for evento in self.cadastrar_eventos:
            if nome_evento == evento.get_nome_evento():
                return evento
        return None

    def identificar_usuario(self, usuario_cadastrado):
        for usuario in self.cadastrar_usuario:
            if usuario.get_usuario() == usuario_cadastrado:
                return usuario
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

    def cadastro_ocorrencia(self, tipo, placa, quantidade_veiculos, data, hora, descricao):
        ocorrencia = self.identificar_ocorrencia(tipo)
        if ocorrencia is None:
            ocorrencia = Ocorrencias(tipo, placa, quantidade_veiculos, data, hora, descricao)
            self.cadastrar_ocorrencia.append(ocorrencia)
            return True
        return False

    def cadastro_evento(self, nome_evento, data_inicial, data_final, vagas):
        eventos = self.identificar_evento(nome_evento)
        if eventos is None:
            eventos = Eventos(nome_evento, data_inicial, data_final, vagas)
            self.cadastrar_eventos.append(eventos)
            return True
        return False

    def cadastro_usuario(self, nome, funcao, setor, matricula, usuario, senha):
        mp_usuario = self.identificar_usuario(nome)
        if mp_usuario is None:
            mp_usuario = Usuario(nome, funcao, setor, matricula, usuario, senha)
            self.cadastrar_usuario.append(mp_usuario)
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

    # LOGIN METHOD
    def login(self, usuario_cadastrado, senha_cadastrada):
        for usuario in self.cadastrar_usuario:
            if usuario_cadastrado == usuario.get_usuario() and senha_cadastrada == usuario.get_senha():
                return True
            else:
                return False


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

    def get_cadastrar_usuario(self):
        return self.cadastrar_usuario

    def set_cadastrar_usuario(self, cadastrar_usuario):
        self.cadastrar_usuario = cadastrar_usuario

    def get_cadastrar_ocorrencia(self):
        return self.cadastrar_ocorrencia

    def set_cadastrar_ocorrencia(self, cadastrar_ocorrencia):
        self.cadastrar_ocorrencia = cadastrar_ocorrencia

    def get_cadastrar_eventos(self):
        return self.cadastrar_eventos

    def set_cadastrar_eventos(self, cadastrar_eventos):
        self.cadastrar_eventos = cadastrar_eventos

















