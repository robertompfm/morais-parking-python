# DATA BASE
DB_NAME = "../morais_parking.db"

# NOMES TABELA
USUARIOS_TABLE = "usuarios"
VEICULOS_TABLE = "veiculos"
PROPRIETARIOS_TABLE = "proprietarios"
AREA_TABLE = "area"
OCORRENCIAS_TABLE = "ocorrencias"
EVENTOS_TABLE = "eventos"

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
                        "(placa TEXT NOT NULL, " + \
                        "modelo TEXT NOT NULL, " + \
                        "cor TEXT NOT NULL, " + \
                        "proprietario TEXT NOT NULL, " + \
                        "tipo TEXT NOT NULL)"

INSERT_VEICULO = "INSERT INTO " + VEICULOS_TABLE + \
                 "(placa, modelo, cor, proprietario, tipo )" + \
                 " VALUES (?, ?, ?, ?, ?)"

DELETE_VEICULO = "DELETE FROM " + VEICULOS_TABLE + \
                 "WHERE placa = ?"

QUERY_VEICULO_BY_PLACA = "SELECT * FROM " + VEICULOS_TABLE + \
                         "WHERE placa = ?"

QUERY_PLACAS_BY_PROPRIETARIO = "SELECT placa FROM " + VEICULOS_TABLE + \
                               " WHERE proprietario = ?"

# PROPRIETARIO
DROP_PROPRIETARIOS_TABLE = "DROP TABLE IF EXISTS " + PROPRIETARIOS_TABLE
CREATE_PROPRIETARIOS_TABLE = "CREATE TABLE IF NOT EXISTS " + PROPRIETARIOS_TABLE + \
                             "(nome TEXT NOT NULL, " + \
                             "matricula TEXT NOT NULL, " + \
                             "curso TEXT NOT NULL)"

INSERT_PROPRIETARIOS = "INSERT INTO " + PROPRIETARIOS_TABLE + \
                       "(nome, matricula, curso)" + \
                       "VALUES (?, ?, ?)"

DELETE_PROPRIETARIOS = "DELETE FROM " + PROPRIETARIOS_TABLE + \
                       "WHERE nome = ?"

QUERY_PROPRIETARIOS_BY_NOME = "SELECT * FROM " + PROPRIETARIOS_TABLE + \
                              "WHERE nome = ?"

# AREA
DROP_AREA_TABLE = "DROP TABLE IF EXISTS " + AREA_TABLE
CREATE_AREA_TABLE = "CREATE TABLE IF NOT EXISTS " + AREA_TABLE + \
                    "(nome TEXT NOT NULL, " + \
                    "capacidade TEXT NOT NULL)"

INSERT_AREA = "INSERT INTO " + AREA_TABLE + \
              "(nome, capacidade)" + \
              "VALUES (?, ?)"

DELETE_AREA = "DELETE FROM " + AREA_TABLE + \
              "WHERE nome = ?"

QUERY_AREA_BY_NOME = "SELECT * FROM " + AREA_TABLE + \
                     "WHERE nome = ?"

# OCORRENCIA
DROP_OCORRENCIA_TABLE = "DROP TABLE IF EXISTS " + OCORRENCIAS_TABLE
CREATE_OCORRENCIA_TABLE = "CREATE A TABLE IF NOT EXISTS " + OCORRENCIAS_TABLE + \
                          "(tipo TEXT NOT NULL, " + \
                          "placa TEXT NOT NULL, " + \
                          "quantidade_veiculos TEXT NOT NULL, " + \
                          "data TEXT NOT NULL," + \
                          "hora TEXT NOT NULL, " \
                          "descricao TEXT NOT NULL)"

INSERT_OCORRENCIA = "INSERT INTO " + OCORRENCIAS_TABLE + \
                    "(tipo, placa, quantidadeveiculos, data, hora, descricao)" + \
                    "VALUES (?, ?, ?, ?, ?, ?)"

QUERY_OCORRENCIA_BY_TIPO = "SELECT * FROM " + OCORRENCIAS_TABLE + \
                           "WHERE tipo = ?"

# EVENTOS
DROP_EVENTO_TABLE = "DROP TABLE IF EXISTS " + EVENTOS_TABLE
CREATE_EVENTO_TABLE = "CREATE A TABLE IF NOT EXISTS " + EVENTOS_TABLE + \
                      "(nome_evento TEXT NOT NULL, " + \
                      "data_inicial TEXT NOT NULL, " + \
                      "data_final TEXT NOT NULL," + \
                      "vagas TEXT NOT NULL)"

INSERT_EVENTO = "INSERT INTO " + EVENTOS_TABLE + \
                "(nome_evento, data_inicial, data_final, vagas)" + \
                "VALUES (?, ?, ?, ?)"

DELETE_EVENTO = "DELETE FROM " + EVENTOS_TABLE + \
                "WHERE nome = ?"

QUERY_EVENTO_BY_NOME = "SELECT * FROM " + EVENTOS_TABLE + \
                       "WHERE nome = ?"
