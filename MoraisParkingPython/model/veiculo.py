

class Veiculo:
    """
    classe Veiculo
    """
    # CONSTRUTOR
    def __init__(self, proprietario, matricula, curso, tipo, placa=""):
        """
        Inicia a classe Veiculo
        :param proprietario: nome do proprietario
        :param matricula: matricula do proprietario
        :param curso: nome do curso do proprietario
        :param tipo: tipo do veiculo (onibus, carro, moto, ou bicicleta)
        :param placa: placa do veiculo
        """
        self.proprietario = proprietario
        self.matricula = matricula
        self.curso = curso
        self.tipo = tipo
        self.placa = placa


    # GETTERS AND SETTERS
    def get_proprietario(self):
        """
        :return: nome do proprietario
        """
        return self.proprietario

    def get_matricula(self):
        """
        :return: numero da matricula do proprietario
        """
        return self.matricula

    def get_curso(self):
        """
        :return: nome do curso do proprietario
        """
        return self.curso

    def get_tipo(self):
        """
        :return: tipo do veiculo (onibus, carro, moto ou bicicleta)
        """
        return self.tipo

    def get_placa(self):
        """
        :return: o numero da placa do veiculo
        """
        return self.placa

    def set_proprietario(self, proprietario):
        """
        altera o nome do proprietario
        """
        self.proprietario = proprietario

    def set_matricula(self, matricula):
        """
        altera o numero da matricula
        """
        self.matricula = matricula

    def set_curso(self, curso):
        """
        altera o nome do curso do proprietario
        """
        self.curso = curso

    def set_tipo(self, tipo):
        """
        altera o tipo do veiculo (onibus, carro, moto ou bicicleta)
        """
        self.tipo = tipo

    def set_placa(self, placa):
        """
        altera o numero da placa do veiculo
        """
        self.placa = placa


    # STR (toString)
    def __str__(self) -> str:
        return "Proprietario: " + self.proprietario + "; Placa: " + self.placa

