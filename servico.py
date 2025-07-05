from robo import inicializar, get_resposta as get_resposta_robo, NOME_ROBO
from flask import Flask, Response

import json

servico = Flask(NOME_ROBO)
inicializado, robo = inicializar()

@servico.get("/")
def get_info():
    info = {
        "descrição": "Robô Especialista em IA",
        "email": "franckallyson@hotmail.com",
        "versão": "1.0"
    }

    return Response(json.dumps(info), status=200, mimetype="application/json")

@servico.get("/resposta/<string:mensagem>")
def get_resposta(mensagem):
    resposta, confianca = get_resposta_robo(robo, mensagem)

    resposta = {
        "resposta": resposta,
        "confianca": confianca
    }

    return Response(json.dumps(resposta), status=200, mimetype="application/json")


if __name__ == "__main__":
    if inicializado:
        servico.run(host="localhost", debug=True)
    else:
        print("não foi possível inicializar o robô")

