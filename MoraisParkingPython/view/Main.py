from model.AreaEstacionamento import AreaEstacionamento
from model.Estacionamento import Estacionamento

from model.Constants import *
from control.controller_login import ControllerLogin
from control.controller_veiculos import ControllerVeiculos
from control.controller_proprietario import ControllerProprietarios
from control.controller_area import ControllerAreaEstacionamento
from control.controller_ocorrencias import ControllerOcorrencia
from control.controller_eventos import ControllerEventos
from View.view_constants import *

morais_parking = Estacionamento(30)
area_estacionamento = AreaEstacionamento("Carros", 10)


menu = "Escolha uma opção: "

class Main():
    def __init__(self):
        self.controllerLogin = ControllerLogin()
        self.usuario = None
        self.controllerVeiculos = ControllerVeiculos()
        self.veiculo = None
        self.controllerProprietarios = ControllerProprietarios()
        self.proprietario = None
        self.controllerArea = ControllerAreaEstacionamento()
        self.area = None
        self.controllerOcorrencias = ControllerOcorrencia()
        self.ocorrencia = None
        self.controllerEventos = ControllerEventos()
        self.eventos = None

    def login(self):
        print("====== MORAIS PARKING ======")
        print("[1] Entrar", "\n[2] Cadastar Usuário", "\n[3] Sair")

        op_menu = int(input(MENU))
        if op_menu == 1:
            self.sign_in()
        elif op_menu == 2:
            self.sign_up()
        elif op_menu == 3:
            quit()
        else:
            print("Opcao invalida")
            self.login()


    def sign_in(self):
        print("====== SIGN IN ======")
        email = input("Email: ")
        senha = input("Senha: ")

        self.usuario = self.controllerLogin.sign_in(email, senha)
        if self.usuario is not None:
            print("OK")
            self.menu()
        else:
            self.login()


    def sign_up(self):
        print("====== SIGN UP ======")
        usuario = input("Usuario: ")
        senha = input("Senha: ")

    def menu(self):
        tipo = self.usuario.get_setor()
        if tipo == ESTACIONAMENTO:
            self.menu_Estacionamento()
        elif tipo == RH:
            self.menu_RH()
        elif tipo == GESTAO:
            self.menu_Gestor()

    def menu_RH(self):
        op_menu = -1
        while op_menu != 3:
            print("====== MORAIS PARKING ======")
            print("[1] Veículo",
                  "\n[2] Proprietário",
                  "\n[3] Sair")

            op_menu = int(input(MENU))
            if op_menu == 1:
                self.mp_veiculo()
            elif op_menu == 2:
                self.mp_proprietario()
            else:
                break

    def menu_Estacionamento(self):
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

    def menu_Gestor(self):
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
                self.mp_estacionamento()

            elif op_menu == 2:
                self.mp_veiculo()

            elif op_menu == 3:
                self.mp_proprietario()

            elif op_menu == 4:
                self.mp_areas()

            elif op_menu == 5:
                self.mp_ocorrencias()

            elif op_menu == 6:
                self.mp_eventos()

            else:
                break


    def mp_estacionamento(self):
        print(
            "  [1] Autorizar Entrada",
            "\n[2] Autorizar Saída",
            "\n[3] Busca Veículo",
            "\n[4] Busca Proprietário",
            "\n[5] Busca Área",
            "\n[6] Status do Estacionamento"
        )

        op_menu = int(input(MENU))

        if op_menu == 1:
            placa = input("Placa: ")
            modelo = input("Veiculo: ")
            cor = input("Cor: ")
            if morais_parking.autorizar_entrada(placa, modelo, cor):
                print("Entrada autorizada")
            else:
                print("Nao foi possivel autorizar a entrada.\nEstacionamento lotado")

        elif op_menu == 2:
            placa = input("Placa: ")
            modelo = input("Modelo: ")
            cor = input("Cor: ")
            if morais_parking.autorizar_saida(placa, modelo, cor):
                print("Saida autorizada")
            else:
                print("Nao foi possivel autorizar a saida.")
                print("Verifique se os dados foram inseridos de forma correta")

        elif op_menu == 3:
            placa = input("Placa: ")
            self.veiculo = self.controllerVeiculos.find_veiculo(placa)

        elif op_menu == 4:
            nome = input("Proprietário: ")
            self.proprietario = self.controllerProprietarios.find_proprietarios(nome)

        elif op_menu == 5:
            nome = input("Área: ")
            area = morais_parking.identificar_area(nome)
            if area == None:
                print("Area nao encontrada")
            else:
                print(area)

        elif op_menu == 6:
            print(morais_parking.get_status())

        else:
            print("Opção Inválida")


    def mp_veiculo(self):
        print("[1] Cadastrar Veículo", "\n[2] Remover Veículo")
        op_menu = int(input(MENU))

        if op_menu == 1:
            placa = input("Placa: ")
            modelo = input("Modelo: ")
            cor = input("Cor: ")
            proprietario = input("Proprietario: ")
            nome_area = input("Área: ")
            self.veiculo = self.controllerVeiculos.register_veiculo(placa, modelo, cor, proprietario, nome_area)

        elif op_menu == 2:
            placa = input("Placa: ")
            self.veiculo = self.controllerVeiculos.remove_veiculo(placa)

        else:
            print("Opção Inválida")


    def mp_proprietario(self):
        print("[1] Cadastrar Proprietário", "\n[2] Remover Proprietário")
        op_menu = int(input(MENU))

        if op_menu == 1:
            nome = input("Proprietário: ")
            matricula = int(input("Matrícula: "))
            curso = input("Curso: ")
            self.proprietario = self.controllerProprietarios.register_proprietario(nome, matricula, curso)

        elif op_menu == 2:
            nome = input("Proprietário: ")
            self.proprietario = self.controllerProprietarios.remove_proprietario(nome)

        else:
            print("Opção Inválida")


    def mp_areas(self):
        print("[1] Cadastrar Área", "\n[2] Verificar Área", "\n[3] Remover Área")
        op_menu = int(input(MENU))

        if op_menu == 1:
            nome = input("Nome da área: ")
            capacidade = int(input("Capacidade: "))
            self.area = self.controllerArea.register_area(nome, capacidade)

        elif op_menu == 2:
            nome = input("Nome da área: ")
            area = morais_parking.identificar_area(nome)
            self.area = self.controllerArea.find_area(nome)


        elif op_menu == 3:
            nome = input("Nome da área: ")
            self.area = self.controllerArea.remove_area(nome)

        else:
            print("Opção Inválida")

    def mp_ocorrencias(self):
        print("[1] Cadastrar Ocorrência", "\n[2] Buscar Ocorrência")
        op_menu = int(input(MENU))

        if op_menu == 1:
            tipo = input("Tipo da ocorrência: ")
            placa = input("Placa: ")
            quantVeiculo = input("Quantidade de veículo: ")
            data = input("Data: ")
            hora = input("Hora: ")
            descricao = input("Descrição: ")
            self.ocorrencia = self.controllerOcorrencias.register_ocorrencia(tipo, placa, quantVeiculo, data, hora, descricao)

        elif op_menu == 2:
            tipo = input("Tipo da ocorrência: ")
            self.ocorrencia = self.controllerOcorrencias.find_ocorrencia(tipo)

        else:
            print("Opção Inválida")

    def mp_eventos(self):
        print("[1] Cadastrar Evento", "\n[2] Buscar Evento", "\n[3] Excluir Evento")
        op_menu = input(MENU)

        if op_menu == 1:
            nome_evento = input("Nome do evento: ")
            data_inicial = input("Data inicial: ")
            data_final = input("Data final: ")
            vagas = input("Quantidade de vagas: ")
            self.eventos = self.controllerEventos.register_evento(nome_evento, data_inicial, data_final, vagas)

        elif op_menu == 2:
            nome_evento = input("Nome do evento: ")
            self.eventos = self.controllerEventos.find_evento(nome_evento)

        elif op_menu == 3:
            nome_evento = input("Nome do evento: ")
            self.eventos = self.controllerEventos.remove_evento(nome_evento)

        else:
            print("Opção Inválida")






main = Main()
main.login()

