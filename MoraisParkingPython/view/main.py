from model.veiculo import Veiculo
from model.proprietario import Proprietario
from model.area_estacionamento import AreaEstacionamento
from model.estacionamento import Estacionamento

morais_parking = Estacionamento(30)
area_estacionamento = AreaEstacionamento("Carros", 10)
carro = Veiculo("Larissa", 20192007035, "Sistemas para Internet", "Carro", "ABC1234")


menu = "Escolha uma opção: "
def opcoes():
    while menu != 5:
        print("====== MORAIS PARKING ======")
        print("\n[1] Estacionamento", "\n[2] Veículo", "\n[3] Proprietário", "\n[4] Áreas", "\n[5] Sair")
        op_Menu = int(input(menu))
        if op_Menu == 1:
            mp_estacionamento()

        elif op_Menu == 2:
            mp_veiculo()

        elif op_Menu == 3:
            mp_proprietario()

        elif op_Menu == 4:
            mp_areas()
        else:
            break


def mp_estacionamento():
    print("\n[1] Autorizar Entrada", "\n[2] Autorizar Saída", "\n[3] Identificar Veículo", "\n[4] Identificar Proprietário", "\n[5] Identificar Área")

    op_Menu = int(input(menu))

    if op_Menu == 1:
        placa = input("Placa: ")
        modelo = input("Veiculo: ")
        cor = input("Cor: ")
        morais_parking.autorizar_entrada(placa, modelo, cor)
        opcoes()

    elif op_Menu == 2:
        placa = input("Placa: ")
        modelo = input("Modelo: ")
        cor = input("Cor: ")
        morais_parking.autorizar_saida(placa, modelo, cor)
        opcoes()

    elif op_Menu == 3:
        placa = input("Placa: ")
        morais_parking.identificar_veiculo(placa)
        opcoes()

    elif op_Menu == 4:
        nome = input("Proprietário: ")
        morais_parking.identificar_proprietario(nome)
        opcoes()

    elif op_Menu == 5:
        nome = input("Área: ")
        morais_parking.identificar_area(nome)
        opcoes()

    else:
        print("Opção Inválida")
        opcoes()


def mp_veiculo():
    print("[1] Cadastrar Veículo", "\n[2] Remover Veículo")
    op_Menu = int(input(menu))

    if op_Menu == 1:
        nome = input("Proprietário: ")
        matricula = int(input("Matrícula: "))
        curso = input("Curso: ")
        placa = input("Placa: ")
        modelo = input("Modelo: ")
        cor = input("Cor: ")
        nome_area = input("Área: ")
        morais_parking.cadastrar_veiculo(nome, matricula, curso, placa, modelo, cor, nome_area)
        opcoes()

    elif op_Menu == 2:
        placa = input("Placa: ")
        morais_parking.excluir_veiculo(placa)
        opcoes()

    else:
        print("Opção Inválida")
        opcoes()


def mp_proprietario():
    print("[1] Cadastrar Proprietário", "\n[2] Remover Proprietário")
    op_Menu = int(input(menu))

    if op_Menu == 1:
        nome = input("Proprietário: ")
        matricula = int(input("Matrícula: "))
        curso = input("Curso: ")
        morais_parking.cadastrar_proprietario(nome, matricula, curso)
        opcoes()

    elif op_Menu == 2:
        nome = input("Proprietário: ")
        morais_parking.excluir_proprietario(nome)
        opcoes()
    else:
        print("Opção Inválida")
        opcoes()


def mp_areas():
    print("[1] Cadastrar Área", "\n[2] Identificar Área", "\n[3] Remover Área", "\n[4] Adicionar Veículo", "\n[5] Remover Veículo")
    op_Menu = int(input(menu))

    if op_Menu == 1:
        nome = input("Área: ")
        capacidade = int(input("Capacidade: "))
        morais_parking.cadastrar_area(nome, capacidade)
        opcoes()

    elif op_Menu == 2:
        nome = input("Área: ")
        morais_parking.identificar_area(nome)
        opcoes()

    elif op_Menu == 3:
        nome = input("Área: ")
        morais_parking.excluir_area(nome)
        opcoes()

    elif op_Menu == 4:
        area_estacionamento.adicionar_veiculo()
        opcoes()

    elif op_Menu == 5:
        area_estacionamento.remover_veiculo()
        opcoes()

    else:
        print("Opção Inválida")
        opcoes()


def main():
    opcoes()
main()
