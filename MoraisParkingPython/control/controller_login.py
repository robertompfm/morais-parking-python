from dao.data_usuarios import DataUsuarios
from model.usuario import Usuario

class ControllerLogin():
    def __init__(self):
        self.data_usuarios = DataUsuarios()

    def sign_up(self, nome, email, senha, setor):
        self.data_usuarios.open()
        usuario = Usuario(nome, email, senha, setor)
        success = self.data_usuarios.insert_usuario(usuario)
        if success:
            print("Usuario cadastrado com sucesso!")
        else:
            print("Nao foi possivel cadastrar o usuario.")
        self.data_usuarios.close()
        return success

    def sign_in(self, email, senha):
        self.data_usuarios.open()
        usuario = self.data_usuarios.query_usuario_by_email(email)
        if usuario is None:
            print("Email nao cadastrado")
        elif usuario.get_senha() != senha:
            print("Usuario ou senha incorreta")
            usuario = None
        self.data_usuarios.close()
        return usuario




# controller = ControllerLogin()
# controller.sign_in("robertompfm@gmail.com", "beto")


