import json
from flask import Flask, render_template, request, redirect, session, flash, url_for


from src.interface.model import Cliente


def start():
    app = Flask(__name__)
    app.secret_key = "root"
    app.debug = True

    @app.route("/")
    @app.route("/index")
    def home():
        if 'cliente' not in session or session['cliente'] == None:
            return render_template("index.html", titulo='home', nome_css=["apresentacao"])
        else:
            json_data: list = json.loads(session['cliente'])
            cliente: Cliente = Cliente(json_data["email"], None, json_data["nome"], json_data["eh_cliente"],
                                       json_data["cidade"], json_data["cnpj"])

            if cliente.eh_cliente:
                return render_template("cliente.html", titulo='home', nome_css=["cliente"])
            else:
                return render_template("estabelecimento.html", titulo='home', nome_css=["estabelecimento"])

    @app.route("/cadastro")
    def cadastro():
        if 'cliente' not in session or session['cliente'] == None:
            return render_template("cadastro.html", titulo='cadastro', nome_css=["cadastro"],
                                   nome_js=["cadastro"])
        return redirect(url_for('home'))

    @app.route("/login")
    def login():
        return render_template("login.html", titulo='login', nome_css=["login"],
                               nome_js=["popup"])

    @app.route("/autentica", methods=['POST',])
    def autentica():
        email = request.form["email"]
        senha = request.form["senha"]
        cliente = Cliente(email, senha)

        if cliente.login():
            session['cliente'] = json.dumps(cliente.estrutura_json())
            return redirect(url_for('home'))
        else:
            flash("Senha ou email incorreto. Tente Novamente.", "error")
            return redirect(url_for('login'))

    @app.route("/nova_conta", methods=['POST',])
    def nova_conta():
        email = request.form["email"]
        senha = request.form["senha"]
        confirmacao = request.form["confirmacao"]

        if senha == confirmacao:
            if request.form["tipo-conta"] == 'cliente':
                nome = request.form["nome_cliente"]
                cidade = request.form["cidade_cliente"]
                cnpj = None
                eh_cliente = True
            else:
                nome = request.form["nome_esta"]
                cidade = request.form["cidade_esta"]
                cnpj = request.form["cnpj_esta"]
                eh_cliente = False

            print("Nova conta: " + str(email) +" | "+ str(senha) +" | "+ str(nome) +" | "+ str(request.form["tipo-conta"]) +" | "+ str(cidade) +" | "+ str(cnpj))

            cliente = Cliente(email, senha, nome, eh_cliente, cidade, cnpj)

            if cliente.cadastrar():
                session['cliente'] = json.dumps(cliente.estrutura_json())
                return redirect(url_for('home'))

        flash("Senha ou email incorreto. Tente Novamente.", "error")
        return redirect(url_for('cadastro'))

    @app.route("/logout")
    def logout():
        session['cliente'] = None
        return redirect(url_for('home'))

    @app.errorhandler(404)
    def pagina_nao_encontrada(error):
        return render_template("pagina_nao_encontrada.html", title="Página não encontrada",
                               nome_css=[]), 404

    app.run()
