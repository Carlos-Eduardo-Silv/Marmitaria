from app import app, init_db

def test_pagina_inicial():
    """A página inicial deve carregar com status 200"""
    app.config["TESTING"] = True
    init_db()
    with app.test_client() as client:
        resposta = client.get("/")
        assert resposta.status_code == 200

def test_pagina_pedidos():
    """A página de pedidos deve carregar"""
    app.config["TESTING"] = True
    init_db()
    with app.test_client() as client:
        resposta = client.get("/pedidos")
        assert resposta.status_code == 200

def test_api_pedidos():
    """A API deve retornar JSON"""
    app.config["TESTING"] = True
    init_db()
    with app.test_client() as client:
        resposta = client.get("/api/pedidos")
        assert resposta.status_code == 200
        assert resposta.is_json

def test_cadastrar_pedido():
    """Cadastrar um pedido deve redirecionar para /pedidos"""
    app.config["TESTING"] = True
    init_db()
    with app.test_client() as client:
        resposta = client.post("/cadastrar", data={
            "cliente": "João Teste",
            "tamanho": "Grande"
        }, follow_redirects=True)
        assert resposta.status_code == 200