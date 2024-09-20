from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Página inicial</p>"


@app.route("/contacts")
def contacts():
    return "<p>Lista de contatos</p>"


@app.route("/new_contact")
def new_contact():
    return "<p>Form para criação de contato</p>"


@app.route("contact/<id>", methods=["POST", "PUT", "DELETE"])
def contact(id):
    # [POST] Criar contato / [DELETE] Deletar contato / [PUT] Atualizar contato
    return id
