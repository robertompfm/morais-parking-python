from model.area_estacionamento import AreaEstacionamento
from model.estacionamento import Estacionamento
from model.constants import *

from control.controller_login import ControllerLogin
from control.controller_veiculos import ControllerVeiculos
from control.controller_proprietario import ControllerProprietario
from control.controller_area import ControllerAreaEstacionamento

from view.view_constants import *
from view.funcoes_funcionario import *

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

    def sign_up(self):
        print("====== NOVO USUARIO ======")
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        print("[1] ")


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
            1: cadastrar_funcionario,
            2: remover_funcionario,
            3: self.logout
        }
        print("\n====== MENU RH ======")
        print("[1] Cadastrar funcionario",
              "\n[2] Remover funcionario",
              "\n[3] Logout")

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
            self.proprietario = self.controllerProprietarios.find_proprietario(nome)

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
            if morais_parking.cadastro_ocorrencia(tipo, placa, quantVeiculo, data, hora, descricao):
                print("Ocorrência cadastrada")
            else:
                print("Não foi possível cadastrar a ocorrência")

        elif op_menu == 2:
            tipo = input("Tipo da ocorrência: ")
            ocorrencia = morais_parking.identificar_ocorrencia(tipo)
            if ocorrencia == None:
                print("Ocorrência não encontrada")
            else:
                print(ocorrencia)

    def mp_eventos(self):
        print("[1] Cadastrar Evento", "\n[2] Buscar Evento")
        op_menu = input(MENU)

        if op_menu == 1:
            nome_evento = input("Nome do evento: ")
            data_inicial = input("Data inicial: ")
            data_final = input("Data final: ")
            vagas = input("Quantidade de vagas: ")
            if morais_parking.cadastro_evento(nome_evento, data_inicial, data_final, vagas):
                print("Evento cadastrado")
            else:
                print("Não foi possível cadastrar o evento")
        elif op_menu == 2:
            nome_evento = input("Nome do evento: ")
            evento = morais_parking.identificar_evento(nome_evento)
            if evento == None:
                print("Evento não encontrado")
            else:
                print(evento)






main = Main()
main.start()

