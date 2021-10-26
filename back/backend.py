from config import app, db, jsonify
from modelo import Cachorros

@app.route("/lista_cachorros")
def lista_cachorros():
    #Resgata dados de Cachorros
    cachorros = db.session.query(Cachorros).all()

    #Aplica método JSON da classe Cachorro a cada elemento da lista
    cachorros_em_json = [ x.json() for x in cachorros ]

    #Converte lista python para JSON
    resposta = jsonify(cachorros_em_json)

    #PERMITE resposta para pedidos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

# Inicia servidor Web
app.run(debug=True)   