from flask import render_template, jsonify, request

from config import *
from modelo import *

@app.route("/")
def inicio():
    return '<h2>Sistema de Cadastro e Listagem. </h2>'+\
            '<br><a href="/cadastrar_dono">Cadastra Dono</a>' +\
            '<br><a href="/cadastrar_veterinario">Cadastra Veterinario</a>' + \
            '<br><a href="/listar_donos">Listar Donos</a>' + \
            '<br><a href="/listar_cachorros">Listar Cachorros</a>' + \
            '<br><a href="/listar_vet">Listar Veterinarios</a>'


            #'<br><a href="/cadastrar_cachorro">Cadastra Cachorro</a>' +\
            #'<br><a href="/cadastrar_consulta">Cadastra Consulta</a>' + \
            #'<br><a href="/cadastrar_tosa">Cadastra Tosa</a>' + \
            #'<br><a href="/listar_consultas">Listar Consultas</a>' + \
            #'<br><a href="/listar_tosas">Listar Tosas</a>'

@app.route("/cadastrar_dono")
def cadastrar_dono():
    return render_template("cadastrar_dono.html")

@app.route("/cadastrar_veterinario")
def cadastrar_vet():
    return render_template("cadastrar_vet.html")

@app.route("/listar_donos")
def listar_donos():
    # obter os donos do cadastro
    donos = db.session.query(Dono).all()
    return render_template("listar_donos.html", listaDonos=donos)

@app.route("/listar_cachorros")
def listar_cachorros():
    # obter os cachorros do cadastro
    cachorro = db.session.query(Cachorro).all()
    return render_template("listar_cachorros.html", listaCachorro=cachorro)

@app.route("/listar_vet")
def listar_vet():
    # obter os veterinarios do cadastro
    vet = db.session.query(Veterinario).all()
    return render_template("listar_veterinarios.html", listaVet=vet)

@app.route("/incluir_dono", methods=['POST'])
def incluir_dono():

    resposta = "Dono incluido com sucesso!"

    nome = request.form['nome']
    cep = request.form['cep']
    numero = request.form['numero']
    complemento = request.form['compl']
    celular = request.form['celular']
    fixo = request.form['fixo']
    emerg = request.form['emerg']
    cachorro = request.form['cachorro']
    idade = request.form['idade']
    if nome != "" and cep != "":
        try:
            novoEndereco = Endereco(cep=cep, numero=numero, compl=complemento)
            if celular != "" or fixo != "" or emerg != "":
                novoTelef = Telefone(celular=celular, fixo=fixo, emerg=emerg)
                novoContato = Contato(endereco=novoEndereco, telefone=novoTelef)
                db.session.add(novoTelef)
                db.session.add(novoContato)
            else:
                novoContato = Contato(endereco=novoEndereco)
                db.session.add(novoContato)
            novaPessoa = Pessoa(nome=nome, contato=novoContato)
            db.session.add(novaPessoa)

            cachorro = Cachorro(nome=cachorro, idade=idade)

            novoDono = Dono(pessoa=novaPessoa, cachorro=cachorro)
            db.session.add(novoDono)

            novoCachorro = Cachorro(nome=cachorro, idade=idade, dono=novoDono)
            db.session.add(novoCachorro)

            db.session.commit()
        except Exception as e:
            resposta = "Falha ao incluir"
        return resposta
    else:
        resposta = "Falha ao incluir!"
        return resposta

@app.route("/incluir_vet", methods=['POST'])
def incluir_veterinario():
    resposta = "Veterinario incluído com sucesso!"

    nome = request.form['nome']
    cep = request.form['cep']
    numero = request.form['numero']
    complemento = request.form['compl']
    celular = request.form['celular']
    fixo = request.form['fixo']
    emerg = request.form['emerg']
    cepC = request.form['cepC']
    numeroC = request.form['numeroC']
    complementoC = request.form['complC']
    sala = request.form['sala']

    if nome != "" and cep != "" and cepC != "":
        try:
            novoEndereco = Endereco(cep=cep, numero=numero, compl=complemento)
            novoEnderecoC = Endereco(cep=cepC, numero=numeroC, compl=complementoC)
            if celular != "" or fixo != "" or emerg != "":
                novoTelef = Telefone(celular=celular, fixo=fixo, emerg=emerg)
                novoContato = Contato(endereco=novoEndereco, telefone=novoTelef)
                db.session.add(novoTelef)
                db.session.add(novoContato)
            else:
                novoContato = Contato(endereco=novoEndereco)
                db.session.add(novoContato)
            novoConsultorio = Consultorio(endereco=novoEnderecoC, sala=sala)
            db.session.add(novoConsultorio)

            novaPessoa = Pessoa(nome=nome, contato=novoContato)
            db.session.add(novaPessoa)

            novoVeterinario = Veterinario(pessoa=novaPessoa, consultorio=novoConsultorio)
            db.session.add(novoVeterinario)

            db.session.commit()
        except Exception as e:
            resposta = "Falha ao incluir"
        return resposta
    else:
        resposta = "Falha ao incluir"
        return resposta

if __name__ == "__main__":

    #Apaga arquivo existente
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    #Criando dados para BD
    p1 = Pessoa(nome = "Cloe", Raca = "FreshPoodle",Idade = "4", Dono = "Juanes")
    d1 = Dono(nome = "Cloe", Raca = "FreshPoodle",Idade = "4", Dono = "Juanes")
    c2 = Cachorros(Nome = "Toby", Raca = "Bulldozer",  Idade = "5", Dono = "Jefritto")
    c3 = Cachorros(Nome = "Tito", Raca = "Vira-lata",  Idade = "1", Dono = "Nicolas")
    c4 = Cachorros(Nome = "Mel",  Raca = "Bulldog",    Idade = "3", Dono = "Mariana")

    #Adiciona Cachorros ao BD
    db.session.add(c1)
    db.session.add(c2)
    db.session.add(c3)
    db.session.add(c4)
    db.session.commit()

app.run(debug=True)