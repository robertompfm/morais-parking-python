class Usuario:

    # CONSTRUTOR
    def __init__(self, nome, funcao, setor, matricula, usuario, senha):
        self.nome = nome
        self.funcao = funcao
        self.setor = setor
        self.matricula = matricula
        self.usuario = usuario
        self.senha = senha

    # GETTERS AND SETTERS
    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_funcao(self):
        return self.funcao

    def set_funcao(self, funcao):
        self.funcao = funcao

    def get_setor(self):
        return self.setor

    def set_setor(self, setor):
        self.setor  = setor

    def get_matricula(self):
        return self.matricula

    def set_matricula(self, matricula):
        self.matricula = matricula

    def get_usuario(self):
        return self.usuario

    def set_usuario(self, usuario):
        self.usuario = usuario

    def get_senha(self):
        return self.senha

    def set_senha(self, senha):
        self.senha = senha

    # STR (toString)
    def __str__(self):
        return "Nome: " + self.nome + "\nFunção: " + self.funcao + "\nSetor: " + self.setor + \
               "\nMatrícula: " + self.matricula + "\nUsuário: " + self.usuario + "\nSenha: " + self.senha

    def __eq__(self, outro):
        return isinstance(outro, Usuario) and outro.usuario == self.usuario
