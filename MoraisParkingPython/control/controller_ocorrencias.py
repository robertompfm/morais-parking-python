from dao.data_ocorrencia import DataOcorrencia
from model.Ocorrencias import Ocorrencias


class ControllerOcorrencia():
    def __init__(self):
        self.data_ocorrencia = DataOcorrencia()

    def register_ocorrencia(self, tipo, placa, quantidade_veiculos, data, hora, descricao):
        self.data_ocorrencia.open()
        ocorrencia = Ocorrencias(tipo, placa, quantidade_veiculos, data, hora, descricao)
        success = self.data_ocorrencia.insert_ocorrencia(ocorrencia)
        if success:
            print("Ocorrência cadastrada com sucesso!")
        else:
            print("Ocorrência não foi cadastrada")
        self.data_ocorrencia.close()
        return success

    def find_ocorrencia(self, tipo):
        self.data_ocorrencia.open()
        ocorrencia = self.data_ocorrencia.query_ocorrencia_by_tipo(tipo)
        if ocorrencia is None:
            print("Ocorrencia não cadastrada!")
        self.data_ocorrencia.close()
        return ocorrencia

