

class Relatorio(object):
    ocupacoes_max = dict()
    ocorrencias = list()
    evento = None

    @classmethod
    def get_ocupacoes_max(cls):
        return cls.ocupacoes_max

    @classmethod
    def set_ocupacoes_max(cls, ocupacoes_max):
        cls.ocupacoes_max = ocupacoes_max

    @classmethod
    def get_ocorrencias(cls):
        return cls.ocorrencias

    @classmethod
    def set_ocorrencias(cls, ocorrencias):
        cls.ocorrencias = ocorrencias

    @classmethod
    def add_ocorrencia(cls, ocorrencia):
        cls.ocorrencias.append(ocorrencia)

    @classmethod
    def del_ocorrencia(cls, ocorrencia):
        cls.ocorrencias.remove(ocorrencia)

    @classmethod
    def get_evento(cls):
        return cls.evento

    @classmethod
    def set_evento(cls, evento):
        cls.evento = evento

