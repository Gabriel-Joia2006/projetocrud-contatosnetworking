# Projeto CRUD 3 Camadas - Cadastro Contatos Networking
# Participantes do Grupo:
#  RA2400853 - Gabriel Joia Costa
#  RA2402270 - Josafa Victor da Costa
from flask import Flask, request, render_template
from dbsp1 import get_connection
import webbrowser
import threading

app = Flask(__name__)


@app.route("/")
def formulario():
    return render_template("cadastrosp1.html")


@app.route("/contatos", methods=["POST"])
def criar_contato():
    nome = request.form["nome"]
    email = request.form["email"]
    telefone = request.form.get("telefone")
    observacoes = request.form.get("observacoes")

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
        INSERT INTO contatos (nome, email, telefone, observacoes)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql, (nome, email, telefone, observacoes))
    conn.commit()

    cursor.close()
    conn.close()

    return render_template("cadastrosp1.html", mensagem="Contato cadastrado com sucesso!")


def abrir_navegador():
    webbrowser.open("http://127.0.0.1:5000")


if __name__ == "__main__":
    threading.Timer(1.0, abrir_navegador).start()
    app.run(debug=True)
