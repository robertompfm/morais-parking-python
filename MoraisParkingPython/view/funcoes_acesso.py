from control.controller_veiculos import ControllerVeiculos
from control.controller_proprietario import ControllerProprietario
from control.controller_permissoes import ControllerPermissoes
from control.controller_area import ControllerAreaEstacionamento
from control.controller_eventos import ControllerEventos

from model.constants import *
from model.evento import Evento
from model.area_estacionamento import AreaEstacionamento
from model.veiculo import Veiculo

from datetime import datetime

controller_veiculo = ControllerVeiculos()
controller_proprietario = ControllerProprietario()
controller_permissoes = ControllerPermissoes()
controller_areas = ControllerAreaEstacionamento()
controller_eventos = ControllerEventos()


def autorizar_entrada():
    print("\n====== AUTORIZAR ENTRADA ======")
    placa = input("Placa: ")
    if len(placa) <= 0:
        print("Placa invalida")
        return
    veiculo = controller_veiculo.find_veiculo(placa)
    if veiculo is None:
        print("Insira dados do veiculo")
        modelo = input("Modelo: ")
        cor = input("Cor: ")
        print("[1] Carro; [2] Motocicleta; [3] Onibus")
        try:
            tipo = TIPO_VEICULO[int(input("Tipo de veiculo (1, 2, ou 3): "))]
        except:
            print("Input invalido")
            return
        veiculo = Veiculo(placa, modelo, cor, None, tipo)

    print(veiculo)

    evento = controller_eventos.find_todays_evento()
    print(evento)




def remover_evento():
    print("\n====== REMOVER EVENTO ======")
    eventos = controller_eventos.find_all_eventos()
    if len(eventos) <= 0:
        print("Nao existem eventos cadastrados")
        return
    print("Eventos:")
    eventos_str = ""
    for i in range(len(eventos)):
        eventos_str += "[{}] {}  ".format((i + 1), eventos[i].get_nome_evento())
    print(eventos_str)
    try:
        evento = eventos[(int(input("Escolha o indice da evento a ser removido: ")) - 1)]
        controller_eventos.remove_evento(evento.get_nome_evento())
    except:
        print("Input invalido. Voce precisa inserir um indice valido")


autorizar_entrada()