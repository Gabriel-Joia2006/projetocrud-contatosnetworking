# Projeto CRUD 3 Camadas - Cadastro de Networking
# Participantes do Grupo:
#  RA2400853 - Gabriel Joia Costa
#  RA2402270 - Josafa Victor da Costa
import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Admin123",
        database="projeto"
    )
