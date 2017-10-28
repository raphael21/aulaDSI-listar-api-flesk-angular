#nome = input('Digite seu nome:')
#print('seu nome é:', nome)

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/alunos")
def hello():
    return jsonify (
       number=6,
       people=[
            {"name": "RAPHAEL"},
            {"name": "DIOGO"},
            {"name": "GABRIELA"},
            {"name": "THAIS"},
            {"name": "SILVANIA"},
            {"name": "JORGE"},
    ]
    )

#print('hello word')

