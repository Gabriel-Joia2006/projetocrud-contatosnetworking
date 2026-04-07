# Projeto CRUD 3 Camadas - Cadastro de Contatos de Networking
# Participantes do Grupo:
#  RA2400853 - Gabriel Joia Costa
#  RA2402270 - Josafa Victor da Costa
from flask import Flask, render_template, request
from db import get_connection
from datetime import datetime
import webbrowser
import threading

app = Flask(__name__)


# Página inicial — Cadastro
@app.route("/")
def cadastro():
    return render_template("cadastro.html")


# Página para digitar o ID e carregar dados
@app.route("/alterar")
def alterar():
    return render_template("alterar.html")


# Salvar novo contato
@app.route("/contatos", methods=["POST"])
def salvar_contato():
    nome = request.form.get("nome")
    email = request.form.get("email")
    telefone = request.form.get("telefone")
    observacoes = request.form.get("observacoes")
    cidade = request.form.get("cidade")
    estado_regiao = request.form.get("estado_regiao")
    pais = request.form.get("pais")
    empresa = request.form.get("empresa")
    profissao = request.form.get("profissao")
    fonte = request.form.get("fonte")

    agora = datetime.now()

    conn = get_connection()
    if conn is None:
        return "Erro de conexão com o banco."

    cursor = conn.cursor()

    sql = """
        INSERT INTO contatos
        (nome, email, telefone, observacoes, cidade, estado_regiao, pais,
         empresa, profissao, fonte, created_at, updated_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    valores = (
        nome, email, telefone, observacoes, cidade, estado_regiao, pais,
        empresa, profissao, fonte, agora, agora
    )

    cursor.execute(sql, valores)
    conn.commit()

    id_novo = cursor.lastrowid

    cursor.close()
    conn.close()

    return render_template(
        "cadastro.html",
        mensagem=f"Contato incluído com sucesso! ID: {id_novo}"
    )


# Carregar dados para edição
@app.route("/editar", methods=["POST"])
def editar():
    id_contato = request.form.get("id")

    conn = get_connection()
    if conn is None:
        return "Erro de conexão com o banco."

    cursor = conn.cursor()

    sql = """
        SELECT id, nome, email, telefone, observacoes, cidade, estado_regiao,
               pais, empresa, profissao, fonte
        FROM contatos
        WHERE id = %s
    """

    cursor.execute(sql, (id_contato,))
    contato = cursor.fetchone()

    cursor.close()
    conn.close()

    if not contato:
        return render_template(
            "alterar.html",
            mensagem="Contato não encontrado para o ID informado."
        )

    return render_template("editar.html", contato=contato)


# Atualizar contato existente
@app.route("/atualizar", methods=["POST"])
def atualizar():
    id_contato = request.form.get("id")
    nome = request.form.get("nome")
    email = request.form.get("email")
    telefone = request.form.get("telefone")
    observacoes = request.form.get("observacoes")
    cidade = request.form.get("cidade")
    estado_regiao = request.form.get("estado_regiao")
    pais = request.form.get("pais")
    empresa = request.form.get("empresa")
    profissao = request.form.get("profissao")
    fonte = request.form.get("fonte")

    agora = datetime.now()

    conn = get_connection()
    if conn is None:
        return "Erro de conexão com o banco."

    cursor = conn.cursor()

    sql = """
        UPDATE contatos
        SET nome = %s,
            email = %s,
            telefone = %s,
            observacoes = %s,
            cidade = %s,
            estado_regiao = %s,
            pais = %s,
            empresa = %s,
            profissao = %s,
            fonte = %s,
            updated_at = %s
        WHERE id = %s
    """

    valores = (
        nome, email, telefone, observacoes, cidade, estado_regiao, pais,
        empresa, profissao, fonte, agora, id_contato
    )

    cursor.execute(sql, valores)
    conn.commit()

    cursor.close()
    conn.close()

    return render_template(
        "alterar.html",
        mensagem=f"Contato ID {id_contato} atualizado com sucesso!"
    )


# Abrir navegador automaticamente
def abrir_navegador():
    webbrowser.open("http://127.0.0.1:5000")


if __name__ == "__main__":
    threading.Timer(1.0, abrir_navegador).start()
    app.run(debug=True)
