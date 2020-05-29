from model.area_estacionamento import AreaEstacionamento
from model.estacionamento import Estacionamento
from model.constants import *

from control.controller_login import ControllerLogin
from control.controller_veiculos import ControllerVeiculos
from control.controller_proprietario import ControllerProprietario
from control.controller_area import ControllerAreaEstacionamento

from view.view_constants import *
from view.funcoes_funcionario import *

# CONSTANTS
START_MENU = {
    1: login,
    2: quit
}

# GLOBAL VARIABLES
usuario = None
veiculo = None
proprietario = None
area = None

# CONTROLLERS
controllerLogin = ControllerLogin()
controllerVeiculos = ControllerVeiculos()
controllerProprietarios = ControllerProprietario()
controllerArea = ControllerAreaEstacionamento()

# START
def start():
    global usuario
    print("/n====== MORAIS PARKING ======")
    usuario = login()
    menu()


# MENUS
def menu():
    tipo = usuario.get_setor()
    if tipo == SETOR[1]:
        menu_estacionamento()
    elif tipo == SETOR[2]:
        menu_rh()
    elif tipo == SETOR[3]:
        menu_gestor()
    else:
        start()


# MENU RH
def menu_rh():
    op_menu = -1
    while op_menu != 3:
        print("\n====== MENU RH ======")
        print("[1] Cadastrar funcionario",
              "\n[2] Remover funcionario",
              "\n[3] Logout")

        op_menu = int(input(MENU))
        if op_menu == 1:
            print("veiculo")
            # mp_veiculo()
        elif op_menu == 2:
            print("prprietario")
            # mp_proprietario()
        else:
            break

# MENU ESTACIONAMENTO
def menu_estacionamento():
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
            print("Estacionamento")
            # mp_estacionamento()

        elif op_menu == 2:
            print("veiculo")
            # mp_veiculo()

        elif op_menu == 3:
            print("proprietario")
            # mp_proprietario()

        elif op_menu == 4:
            print("ocorrencias")
            # mp_ocorrencias()

        elif op_menu == 5:
            print("eventos")
            # mp_eventos()
        else:
            break

# MENU GESTOR
def menu_gestor():
    op_menu = -1
    while op_menu != 7:
        print("====== MORAIS PARKING ======")
        print(

            "[1] Estacionamento",
            "\n[2] Veículo",
            "\n[3] Proprietário",
            "\n[4] Áreas",
            "\n[5] Ocorrências"
            "\n[6] Eventos"
            "\n[7] Sair"
        )

        op_menu = int(input(MENU))
        if op_menu == 1:
            print("estacionamento")
            # mp_estacionamento()

        elif op_menu == 2:
            print("veiculo")
            # mp_veiculo()

        elif op_menu == 3:
            print("proprietario")
            # mp_proprietario()

        elif op_menu == 4:
            print("areas")
            # mp_areas()

        elif op_menu == 5:
            print("ocorrencias")
            # mp_ocorrencias()

        elif op_menu == 6:
            print("eventos")
            # mp_eventos()

        else:
            break
