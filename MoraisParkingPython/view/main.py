from model.veiculo import Veiculo
from model.proprietario import Proprietario
from model.area_estacionamento import AreaEstacionamento
from model.estacionamento import Estacionamento
from model.usuario import Usuario
from model.constants import *

from control.controller_login import ControllerLogin

from view.view_constants import *

morais_parking = Estacionamento(30)
area_estacionamento = AreaEstacionamento("Carros", 10)
carro = Veiculo("Larissa", 20192007035, "Sistemas para Internet", "Comum", "ABC1234")

menu = "Escolha uma opção: "

class Main():
    def __init__(self):
        self.controller = ControllerLogin()
        self.usuario = None


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

        self.usuario = self.controller.sign_in(email, senha)
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
            veiculo = morais_parking.identificar_veiculo(placa)
            if veiculo == None:
                print("Veiculo nao cadastrado.")
            else:
                print(veiculo)

        elif op_menu == 4:
            nome = input("Proprietário: ")
            proprietario = morais_parking.identificar_proprietario(nome)
            if proprietario == None:
                print("Proprietario nao cadastrado")
            else:
                print(proprietario)

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
            nome = input("Proprietário: ")
            matricula = int(input("Matrícula: "))
            curso = input("Curso: ")
            placa = input("Placa: ")
            modelo = input("Modelo: ")
            cor = input("Cor: ")
            nome_area = input("Área: ")
            if morais_parking.cadastrar_veiculo(nome, matricula, curso, placa, modelo, cor, nome_area):
                print("Veiculo cadastrado com sucesso")
            else:
                print("Nao foi possivel cadastrar o veiculo")

        elif op_menu == 2:
            placa = input("Placa: ")
            if morais_parking.excluir_veiculo(placa):
                print("Veiculo removido do cadastro")
            else:
                print("Veiculo nao encontrado")

        else:
            print("Opção Inválida")


    def mp_proprietario(self):
        print("[1] Cadastrar Proprietário", "\n[2] Remover Proprietário")
        op_menu = int(input(MENU))

        if op_menu == 1:
            nome = input("Proprietário: ")
            matricula = int(input("Matrícula: "))
            curso = input("Curso: ")
            if morais_parking.cadastrar_proprietario(nome, matricula, curso):
                print("Proprietario cadastrado com sucesso")
            else:
                print("Nao foi possivel cadastrar o proprietario")

        elif op_menu == 2:
            nome = input("Proprietário: ")
            if morais_parking.excluir_proprietario(nome):
                print("Proprietario removido do cadastro")
            else:
                print("Proprietario nao encontrado no cadastro")
        else:
            print("Opção Inválida")


    def mp_areas(self):
        print("[1] Cadastrar Área", "\n[2] Verificar Área", "\n[3] Remover Área")
        op_menu = int(input(MENU))

        if op_menu == 1:
            nome = input("Nome da área: ")
            capacidade = int(input("Capacidade: "))
            if morais_parking.cadastrar_area(nome, capacidade):
                print("Area cadastrada com sucesso")
            else:
                print("Nao foi possivel cadastrar a area")

        elif op_menu == 2:
            nome = input("Nome da área: ")
            area = morais_parking.identificar_area(nome)
            if area == None:
                print("Area nao encontrada")
            else:
                print(area)

        elif op_menu == 3:
            nome = input("Nome da área: ")
            morais_parking.excluir_area(nome)

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
main.login()

