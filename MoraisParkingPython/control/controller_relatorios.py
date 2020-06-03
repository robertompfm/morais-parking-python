from model.estacionamento import Estacionamento
estacionamento = Estacionamento(30)

def status_estacionamento():
    arquivo = open('status_estacionamento.txt', 'w')
    #arquivo.write('Morais Parking\n')
    arquivo.write(estacionamento.get_status())
    arquivo.close()

    arquivo = open('status_estacionamento.txt', 'r')
    for linha in arquivo:
        linha = linha.rstrip()
        print(linha)
    arquivo.close()


def main():
    print(status_estacionamento())

main()









