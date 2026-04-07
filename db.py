# Projeto CRUD 3 Camadas - Cadastro de Contatos de Networking
# Participantes do Grupo:
#  RA2400853 - Gabriel Joia Costa
#  RA2402270 - Josafa Victor da Costa
# Projeto CRUD 3 Camadas - Cadastro de Contatos de Networking
# Participantes do Grupo:
#  RA2400853 - Gabriel Joia Costa
#  RA2402270 - Josafa Victor da Costa
import mysql.connector
from mysql.connector import Error


def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Admin123",
            database="projeto"
        )
        return conn
    except Error as e:
        print("Erro ao conectar:", e)
        return None
