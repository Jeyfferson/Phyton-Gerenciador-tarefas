import sqlite3

from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)

DATABASE = "tarefas.db"


def conectar_banco():
    conexao = sqlite3.connect(DATABASE)
    conexao.row_factory = sqlite3.Row
    return conexao


def inicializar_banco():
    conexao = conectar_banco()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            concluida INTEGER NOT NULL DEFAULT 0
        )
    """)

    conexao.commit()
    conexao.close()


@app.route("/")
def index():
    conexao = conectar_banco()

    tarefas = conexao.execute("""
        SELECT id, titulo, concluida
        FROM tarefas
        ORDER BY concluida ASC, id DESC
    """).fetchall()

    conexao.close()

    return render_template("index.html", tarefas=tarefas)


@app.route("/adicionar", methods=["POST"])
def adicionar():
    titulo = request.form.get("titulo", "").strip()

    if titulo:
        conexao = conectar_banco()

        conexao.execute(
            "INSERT INTO tarefas (titulo) VALUES (?)",
            (titulo,)
        )

        conexao.commit()
        conexao.close()

    return redirect(url_for("index"))


@app.route("/concluir/<int:tarefa_id>", methods=["POST"])
def concluir(tarefa_id):
    conexao = conectar_banco()

    conexao.execute("""
        UPDATE tarefas
        SET concluida = CASE
            WHEN concluida = 0 THEN 1
            ELSE 0
        END
        WHERE id = ?
    """, (tarefa_id,))

    conexao.commit()
    conexao.close()

    return redirect(url_for("index"))


@app.route("/excluir/<int:tarefa_id>", methods=["POST"])
def excluir(tarefa_id):
    conexao = conectar_banco()

    conexao.execute(
        "DELETE FROM tarefas WHERE id = ?",
        (tarefa_id,)
    )

    conexao.commit()
    conexao.close()

    return redirect(url_for("index"))


if __name__ == "__main__":
    inicializar_banco()
    app.run(debug=True)
