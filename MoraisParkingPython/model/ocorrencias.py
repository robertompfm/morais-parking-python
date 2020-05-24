class Ocorrencias():

    # CONSTRUTOR
    def __init__(self, tipo, placa, quantidade_veiculos, data, hora, descricao):
        self.tipo = tipo
        self.placa = placa
        self.quantidade_veiculos = quantidade_veiculos
        self.data = data
        self.hora = hora
        self.descricao = descricao

    # GETTERS AND SETTERS
    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_placa(self):
        return self.placa

    def set_placa(self, placa):
        self.tipo = placa

    def get_quantidade_veiculos(self):
        return self.quantidade_veiculos

    def set_quantidade_veiculos(self, quantidade_veiculos):
        self.quantidade_veiculos = quantidade_veiculos

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_hora(self):
        return self.hora

    def set_hora(self, hora):
        self.hora = hora

    def get_descricao(self):
        return self.descricao

    def set_descricao(self, descricao):
        self.descricao = descricao

    # STR (toString)
    def __str__(self):
        return "Tipo da Ocorrência: " + self.tipo + "\nPlaca: " + self.placa +"\nQuantida de Veículos: " + self.quantidade_veiculos + \
               "\nData: " + self.data + "\nHora: " + self.hora + "\nDescrição: " + self.descricao