class Eventos():

    # CONSTRUTOR
    def __init__(self, nome_evento, data_inicial, data_final, vagas):
        self.nome_evento = nome_evento
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.vagas = vagas

    # GETTERS AND SETTERS
    def get_nome_evento(self):
        return self.nome_evento

    def set_nome_evento(self, nome_evento):
        self.nome_evento = nome_evento

    def get_data_inicial(self):
        return self.data_inicial

    def set_data_inicial(self, data_inicial):
        self.data_inicial = data_inicial

    def get_data_final(self):
        return self.data_final

    def set_data_final(self, data_final):
        self.data_final = data_final

    def get_vagas(self):
        return self.vagas

    def set_vagas(self, vagas):
        self.vagas = vagas

    # STR (toString)
    def __str__(self):
        return "Nome do evento: " + self.nome_evento + "\nData inicial: " + self.data_inicial + \
               "\nData Final: " + self.data_final + "\nVagas: " + self.vagas
