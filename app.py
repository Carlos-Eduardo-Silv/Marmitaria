from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)
DB = "database.db"

def init_db():
    conn = sqlite3.connect(DB)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            tamanho TEXT NOT NULL,
            data TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/pedidos")
def listar_pedidos():
    conn = sqlite3.connect(DB)
    pedidos = conn.execute("SELECT id, cliente, tamanho, data FROM pedidos ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("pedidos.html", pedidos=pedidos)

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    cliente = request.form.get("cliente", "").strip()
    tamanho = request.form.get("tamanho", "").strip()
    if not cliente or not tamanho:
        return redirect(url_for("inicio", erro=1))
    conn = sqlite3.connect(DB)
    conn.execute("INSERT INTO pedidos (cliente, tamanho) VALUES (?, ?)", (cliente, tamanho))
    conn.commit()
    conn.close()
    return redirect(url_for("listar_pedidos"))

@app.route("/api/pedidos")
def api_pedidos():
    conn = sqlite3.connect(DB)
    rows = conn.execute("SELECT id, cliente, tamanho FROM pedidos").fetchall()
    conn.close()
    return jsonify([{"id": r[0], "cliente": r[1], "tamanho": r[2]} for r in rows])

init_db()

if __name__ == "__main__":
    app.run(debug=True)