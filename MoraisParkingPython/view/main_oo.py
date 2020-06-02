from model.area_estacionamento import AreaEstacionamento
from model.estacionamento import Estacionamento
from model.constants import *

from control.controller_login import ControllerLogin
from control.controller_veiculos import ControllerVeiculos
from control.controller_proprietario import ControllerProprietario
from control.controller_area import ControllerAreaEstacionamento

from view.view_constants import *
from view.funcoes_funcionario import *
from view.funcoes_proprietario import *
from view.funcoes_veiculo import *
from view.funcoes_areas import *
from view.funcoes_permissoes import *
from view.funcoes_eventos import *

morais_parking = Estacionamento(30)
area_estacionamento = AreaEstacionamento("Carros", 10)


menu = "Escolha uma opção: "




class Main():
    def __init__(self):
        self.controllerLogin = ControllerLogin()
        self.controllerVeiculos = ControllerVeiculos()
        self.controllerProprietarios = ControllerProprietario()
        self.controllerArea = ControllerAreaEstacionamento()

        self.usuario = None
        self.veiculo = None
        self.proprietario = None
        self.area = None

    def start(self):
        print("\n====== MORAIS PARKING ======")
        print("[1] Entrar", "\n[2] Sair")

        op_menu = int(input(MENU))
        if op_menu == 1:
            self.login()
        elif op_menu == 2:
            quit()
        else:
            print("Opcao invalida")
            self.start()

    def login(self):
        self.usuario = login()
        self.menu()

    # def sign_up(self):
    #     print("====== NOVO USUARIO ======")
    #     nome = input("Nome: ")
    #     email = input("Email: ")
    #     senha = input("Senha: ")
    #     print("[1] ")
    #

    def menu(self):
        if self.usuario is None:
            self.start()
            return
        tipo = self.usuario.get_setor()
        if tipo == SETOR[1]:
            self.menu_estacionamento()
        elif tipo == SETOR[2]:
            self.menu_rh()
        elif tipo == SETOR[3]:
            self.menu_gestor()


    def logout(self):
        self.usuario = None


    def menu_rh(self):
        opcoes = {
            1: cadastrar_proprietario,
            2: remover_proprietario,
            3: cadastrar_veiculo,
            4: remover_veiculo,
            5: conceder_permissao,
            6: remover_permissao,
            7: cadastrar_funcionario,
            8: remover_funcionario,
            9: self.logout
        }
        print("\n====== MENU RH ======")
        print("[1] Cadastrar proprietario",
              "\n[2] Remover proprietario",
              "\n[3] Cadastrar veiculo",
              "\n[4] Remover veiculo",
              "\n[5] Conceder permissao",
              "\n[6] Remover proprietario",
              "\n[7] Cadastrar veiculo",
              "\n[8] Remover veiculo",
              "\n[9] Logout")

        try:
            op_menu = int(input(MENU))
            opcoes[op_menu]()
        except:
            print("Opcao invalida")
            self.menu_rh()
        self.menu()


    def menu_estacionamento(self):
        op_menu = -1
        while op_menu != 6:
            print("====== MORAIS PARKING ======")
            print("[1]Estacionamento",
                  "\n[2] Veículo",
                  "\n[3] Proprietário",
                  "\n[4] Ocorrências"
                  "\n[5] Eventos"
                  "\n[6] Sair")

            op_menu = int(input(MENU))
            if op_menu == 1:
                self.mp_estacionamento()
            elif op_menu == 2:
                self.mp_veiculo()
            elif op_menu == 3:
                self.mp_proprietario()
            elif op_menu == 4:
                self.mp_ocorrencias()
            elif op_menu == 5:
                self.mp_eventos()
            else:
                break


    def menu_gestor(self):
        opcoes = {
            1: cadastrar_funcionario,
            2: remover_funcionario,
            3: cadastrar_area_especial,
            4: remover_area_especial,
            5: cadastrar_evento,
            6: remover_evento,
            7: self.logout
        }
        print("\n====== MENU RH ======")
        print("[1] Cadastrar funcionario",
              "\n[2] Remover funcionario",
              "\n[3] Cadastrar area especial",
              "\n[4] Remover area especial",
              "\n[5] Cadastrar evento",
              "\n[6] Remover evento",
              "\n[7] Logout")

        try:
            op_menu = int(input(MENU))
            opcoes[op_menu]()
        except:
            print("Opcao invalida")
            self.menu_rh()
        self.menu()



main = Main()
main.start()

