from model.veiculo import Veiculo
from model.proprietario import Proprietario
from model.area_estacionamento import AreaEstacionamento
from model.estacionamento import Estacionamento

morais_parking = Estacionamento(30)
area_estacionamento = AreaEstacionamento("Carros", 10)
carro = Veiculo("Larissa", 20192007035, "Sistemas para Internet", "Comum", "ABC1234")


menu = "Escolha uma opção: "
def opcoes():
    while menu != 5:
        print("====== MORAIS PARKING ======")
        print(
            "\n[1] Estacionamento",
            "\n[2] Veículo",
            "\n[3] Proprietário",
            "\n[4] Áreas",
            "\n[5] Sair"
        )

        op_menu = int(input(menu))
        if op_menu == 1:
            mp_estacionamento()

        elif op_menu == 2:
            mp_veiculo()

        elif op_menu == 3:
            mp_proprietario()

        elif op_menu == 4:
            mp_areas()
        else:
            break


def mp_estacionamento():
    print(
        "\n[1] Autorizar Entrada",
        "\n[2] Autorizar Saída",
        "\n[3] Busca Veículo",
        "\n[4] Busca Proprietário",
        "\n[5] Busca Área",
        "\n[6] Status do Estacionamento"
    )

    op_menu = int(input(menu))

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


def mp_veiculo():
    print("[1] Cadastrar Veículo", "\n[2] Remover Veículo")
    op_menu = int(input(menu))

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


def mp_proprietario():
    print("[1] Cadastrar Proprietário", "\n[2] Remover Proprietário")
    op_menu = int(input(menu))

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


def mp_areas():
    print("[1] Cadastrar Área", "\n[2] Verificar Área", "\n[3] Remover Área")
    op_menu = int(input(menu))

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


def main():
    opcoes()
main()
