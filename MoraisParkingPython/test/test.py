from model.veiculo import Veiculo
from model.proprietario import Proprietario
from model.area_estacionamento import AreaEstacionamento
from model.estacionamento import Estacionamento

roberto = Proprietario("Roberto", 20192007007, "Sistemas para Internet")
ford_ka = Veiculo("QFI7289", "Ford Ka", "Preto", roberto, "Estudante")
kombi_domino = Veiculo("D0M1N0", "Kombi", "Cinza")
estudante = AreaEstacionamento("Estudante", 10)
elite = AreaEstacionamento("Elite", -2) # tentando criar com numero negativo
mp_uniesp = Estacionamento(30)

def test_proprietario():
    print(roberto)
    print(roberto.get_curso())

def test_veiculo():
    print(ford_ka)
    print(kombi_domino)

def test_area_estacionamento():
    print(estudante)
    estudante.adicionar_veiculo(ford_ka)
    print(estudante)
    estudante.remover_veiculo(kombi_domino)
    print(estudante)
    # venndo se funciona com mesma placa, mas modelo e proprietario diferente
    estudante.remover_veiculo(Veiculo("QFI7289", "Brasilia", "Amarela"))
    print(estudante)
    print(elite)

def test_estacionamento():
    # print(mp_uniesp.get_status())
    mp_uniesp.cadastrar_area("Estudante", 10)
    mp_uniesp.cadastrar_area("Elite", -2) # teste com numero de vagas negativo
    # print(mp_uniesp.get_status())
    mp_uniesp.cadastrar_proprietario("Roberto", 20192007007, "Sistemas para Internet")
    mp_uniesp.cadastrar_proprietario("Park Saeroi", 123456789, "Gastronomia")
    mp_uniesp.cadastrar_veiculo("Roberto", "144", "n sei", "QFI7289", "Ford Ka", "Preto", "Estudante")
    mp_uniesp.cadastrar_veiculo("Larissa", "20192007***", "SpI", "7777", "Jangga", "Verde", "Elite")
    mp_uniesp.cadastrar_veiculo("Roberto", "", "", "QFI7289", "", "", "")
    mp_uniesp.cadastrar_veiculo("Iria", "20192007***", "SpI", "V1D4L0K4", "HB20", "Vermelho", "Dan Ban")
    mp_uniesp.cadastrar_veiculo("Iria", "20192007***", "SpI", "V1D4L0K4", "HB20", "Vermelho", "Elite")
    print(len(mp_uniesp.get_prop_cadastrados())) # esperado = 4
    print(len(mp_uniesp.get_veiculos_cadastrados()))
    mp_uniesp.autorizar_entrada("V1D4L0K4", "HB20", "Vermelho")
    mp_uniesp.autorizar_entrada("QFI7289", "Ford Ka", "Preto")
    mp_uniesp.autorizar_entrada("V1D4L0K4", "", "")
    mp_uniesp.autorizar_entrada("7777", "", "")
    mp_uniesp.autorizar_entrada("K0MB1", "", "")
    # print(mp_uniesp.get_status())
    mp_uniesp.autorizar_saida("B1N60", "Gol", "Branco")
    mp_uniesp.autorizar_saida("V1D4L0K4", "", "Vermelho")
    mp_uniesp.autorizar_saida("QFI7289", "Ford", "Preto")
    mp_uniesp.autorizar_saida("7777", "", "")
    mp_uniesp.autorizar_saida("K0MB1", "", "")
    print(mp_uniesp.get_status())


# test_proprietario()
# test_veiculo()
# test_area_estacionamento()
test_estacionamento()
