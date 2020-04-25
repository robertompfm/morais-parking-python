from model.proprietario import Proprietario


class Veiculo:

    # CONSTRUTOR
    def __init__(self, placa, modelo, cor, proprietario=Proprietario("Desconhecido", 0, "N/A"), nome_area="Comum"):
        self.placa = placa
        self.proprietario = proprietario
        self.modelo = modelo
        self.cor = cor
        self.nome_area = nome_area

    # GETTERS AND SETTERS
    def get_placa(self):
        return self.placa

    def set_placa(self, placa):
        self.placa = placa

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_cor(self, cor):
        return self.cor

    def set_cor(self, cor):
        self.cor = cor

    def get_proprietario(self):
        return self.proprietario

    def set_proprietario(self, proprietario):
        self.proprietario = proprietario

    def get_area(self):
        return self.nome_area

    def set_area(self, nome_area):
        self.nome_area = nome_area

    # STR (toString)
    def __str__(self):
        return "Veiculo: " + self.modelo + " " + self.cor + " (" + self.placa + \
               ") ; Proprietario: " + str(self.proprietario)

    # EQ (equals)
    def __eq__(self, other):
        return isinstance(other, Veiculo) and other.placa == self.placa

    # NE (not equals)
    def __ne__(self, other):
        not self == other
