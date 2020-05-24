# DATA BASE
DB_NAME = "../morais_parking.db"

# NOMES TABELA
USUARIOS_TABLE = "usuarios"


# USUARIO
DROP_USUARIOS_TABLE = "DROP TABLE IF EXISTS " + USUARIOS_TABLE
CREATE_USUARIOS_TABLE = "CREATE TABLE IF NOT EXISTS " + USUARIOS_TABLE + \
                        " (_id INTEGER PRIMARY KEY," + \
                        " nome TEXT NOT NULL," +\
                        " email TEXT NOT NULL UNIQUE," + \
                        " senha TEXT NOT NULL," + \
                        " setor TEXT NOT NULL)"

INSERT_USUARIO = "INSERT INTO " + USUARIOS_TABLE + \
                 " (nome, email, senha, setor)" + \
                 " VALUES (?, ?, ?, ?)"

DELETE_USUARIO = "DELETE FROM " + USUARIOS_TABLE + \
                 " WHERE email = ?"

QUERY_USUARIO_BY_EMAIL = "SELECT * FROM " + USUARIOS_TABLE + \
                         " WHERE email = ?"

