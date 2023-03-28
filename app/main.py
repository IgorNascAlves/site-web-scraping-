# Importando os módulos necessários
import json
import flask
from flask_cors import CORS, cross_origin
from threading import Thread
from datetime import datetime


def filtrar_por_regiao(dados, regiao=None, ano=None):
  criterios_regioes = {
    'norte': ['AC', 'AM', 'AP', 'PA', 'RO', 'RR', 'TO'],
    'nordeste': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
    'centro-oeste': ['DF', 'GO', 'MT', 'MS'],
    'sudeste': ['ES', 'MG', 'RJ', 'SP'],
    'sul': ['PR', 'RS', 'SC']
  }


  dados_filtrados = []
  for d in dados:
    estado = d.get('Local da compra')
    data_compra = d.get('Data da Compra')
    if (not regiao or estado and estado.upper() in criterios_regioes.get(regiao, [])) and \
            (not ano or data_compra and datetime.strptime(data_compra, '%d/%m/%Y').year == ano):
      dados_filtrados.append(d)

  return dados_filtrados



app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSON_SORT_KEYS'] = False

with open("dados_ecomerce.json", encoding='utf-8') as f:
  dados = json.load(f)



@app.route('/')
def home():
  return "Olá, sou a API"


@app.route("/produtos")
@cross_origin()
def produtos():

  regiao = flask.request.args.get("regiao", default=None, type=str)
  ano = flask.request.args.get("ano", default=None, type=int)

  dados_filtrados = filtrar_por_regiao(dados, regiao, ano)

  return flask.jsonify(dados_filtrados)


def run():
  app.run(host='0.0.0.0')

def keep_alive():
  t = Thread(target=run)
  t.start()

if __name__ == "__main__":
  keep_alive()
