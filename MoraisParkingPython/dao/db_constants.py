# DATA BASE
DB_NAME = "../morais_parking.db"

# NOMES TABELA
USUARIOS_TABLE = "usuarios"
VEICULOS_TABLE = "veiculos"
PROPRIETARIOS_TABLE = "proprietarios"
AREA_TABLE = "area"

# USUARIO
DROP_USUARIOS_TABLE = "DROP TABLE IF EXISTS " + USUARIOS_TABLE
CREATE_USUARIOS_TABLE = "CREATE TABLE IF NOT EXISTS " + USUARIOS_TABLE + \
                        " (_id INTEGER PRIMARY KEY," + \
                        " nome TEXT NOT NULL," + \
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

# VEICULO
DROP_VEICULOS_TABLE = "DROP TABLE IF EXISTS " + VEICULOS_TABLE
CREATE_VEICULOS_TABLE = "CREATE TABLE IF NOT EXISTS " + VEICULOS_TABLE + \
                        "(placa TEXT NOT NULL UNIQUE, " + \
                        "modelo TEXT NOT NULL, " + \
                        "cor TEXT NOT NULL, " + \
                        "proprietario TEXT NOT NULL, " + \
                        "tipo TEXT NOT NULL)"

INSERT_VEICULO = "INSERT INTO " + VEICULOS_TABLE + \
                 "(placa, modelo, cor, proprietario, tipo)" + \
                 " VALUES (?, ?, ?, ?, ?)"

DELETE_VEICULO = "DELETE FROM " + VEICULOS_TABLE + \
                 " WHERE placa = ?"

QUERY_VEICULO_BY_PLACA = "SELECT * FROM " + VEICULOS_TABLE + \
                         " WHERE placa = ?"

QUERY_PLACAS_BY_PROPRIETARIO = "SELECT placa FROM " + VEICULOS_TABLE + \
                               " WHERE proprietario = ?"


# PROPRIETARIO
DROP_PROPRIETARIOS_TABLE = "DROP TABLE IF EXISTS " + PROPRIETARIOS_TABLE
CREATE_PROPRIETARIOS_TABLE = "CREATE TABLE IF NOT EXISTS " + PROPRIETARIOS_TABLE + \
                             " (nome TEXT NOT NULL UNIQUE, " + \
                             " matricula TEXT, " + \
                             " curso TEXT)"

INSERT_PROPRIETARIOS = "INSERT INTO " + PROPRIETARIOS_TABLE + \
                       "(nome, matricula, curso)" + \
                       " VALUES (?, ?, ?)"

DELETE_PROPRIETARIO = "DELETE FROM " + PROPRIETARIOS_TABLE + \
                       " WHERE nome = ?"

QUERY_PROPRIETARIO_BY_NOME = "SELECT * FROM " + PROPRIETARIOS_TABLE + \
                              " WHERE nome = ?"


# AREA
DROP_AREA_TABLE = "DROP TABLE IF EXISTS " + AREA_TABLE
CREATE_AREA_TABLE = "CREATE TABLE IF NOT EXISTS " + AREA_TABLE + \
                    " (nome TEXT NOT NULL," + \
                    " capacidade TEXT NOT NULL)"

INSERT_AREA = "INSERT INTO " + AREA_TABLE + \
              " (nome, capacidade)" + \
              " VALUES (?, ?)"

DELETE_AREA = "DELETE FROM " + AREA_TABLE + \
              "WHERE nome = ?"

QUERY_AREA_BY_NOME = "SELECT * FROM " + AREA_TABLE + \
                     "WHERE nome = ?"

