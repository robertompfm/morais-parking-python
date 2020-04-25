


class AreaEstacionamento():

    # CONSTRUCTOR
    def __init__(self, nome, capacidade):
        self.nome = nome
        self.capacidade = capacidade if capacidade > 0 else 1
        self.veiculos = list()
        self.taxa_ocupacao = 0.0

    # SPECIFIC METHODS
    def atualizar_taxa_ocupacao(self):
        self.taxa_ocupacao = len(self.veiculos) / self.capacidade

    def adicionar_veiculo(self, veiculo):
        if veiculo == None:
            return False
        if len(self.veiculos) >= self.capacidade:
            return False
        if not veiculo in self.veiculos:
            self.veiculos.append(veiculo)
            self.atualizar_taxa_ocupacao()
            return True
        return False

    def remover_veiculo(self, veiculo):
        if veiculo == None:
            return False
        if veiculo in self.veiculos:
            self.veiculos.remove(veiculo)
            self.atualizar_taxa_ocupacao()
            return True
        return False

    # GETTERS AND SETTERS
    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_capacidade(self):
        return self.capacidade

    def set_capacidade(self, capacidade):
        self.capacidade = capacidade

    def get_veiculos(self):
        return self.veiculos

    def set_veiculos(self, veiculos):
        self.veiculos = veiculos

    def get_ocupacao(self):
        return len(self.veiculos)

    def get_taxa_ocupacao(self):
        return self.taxa_ocupacao

    # STR (toString)
    def __str__(self):
        return "Area: {0}; ocupacao: {1} / {2} ({3:.2f}%)".format(
            self.nome, len(self.veiculos), self.capacidade, (self.get_taxa_ocupacao() * 100)
        )


