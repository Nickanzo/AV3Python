
#imports
from flask_sqlalchemy import SQLAlchemy
from flask            import Flask#, jsonify
import os

#CONFIG
app = Flask(__name__)

#Caminho Arquivo BD
path = os.path.dirname(os.path.abspath(__file__))
#Nome de Arquivo
arquivobd = os.path.join(path, 'cachorros.db')

#SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
#Ignora Avisos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)