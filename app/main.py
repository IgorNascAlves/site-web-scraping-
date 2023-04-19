# Importando os módulos necessários
import json
import random
from flask import request, make_response, jsonify, render_template, Flask
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



app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

with open("app/dados/dados_ecomerce.json", encoding='utf-8') as f:
  dados = json.load(f)



@app.route('/')
def home():
  return render_template('index.html')

@app.route('/hello-world')
def hello_world():
  return render_template('hello-world.html')


@app.route("/produtos")
def produtos():

  regiao = request.args.get("regiao", default=None, type=str)
  ano = request.args.get("ano", default=None, type=int)

  dados_filtrados = filtrar_por_regiao(dados, regiao, ano)

  return jsonify(dados_filtrados)


@app.route('/2/tweets/search/recent')
def search_recent_tweets():
    # Extrai os parâmetros da query da requisição
    query = request.args.get('query')
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')


    # Converte as datas para o formato correto
    start_date = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S.%fZ')
    end_date = datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%S.%fZ')

    # Gera uma lista de tweets fictícios usando a API mock
    texts = [
        "Este é um tweet fictício sobre " + query,
        "Outro tweet fictício relacionado a " + query,
        "Um terceiro tweet fictício sobre " + query,
        "Tweet fictício gerado automaticamente sobre " + query,
        "Tweet fictício criado usando inteligência artificial para falar sobre " + query
    ]

    # Monta a resposta com os tweets fictícios gerados
    tweets = []
    for i in range(10):
        tweet = {
            'edit_history_tweet_ids': [random.randint(0, 100)],
            'author_id': str(random.randint(0, 100)),
            'created_at': (start_date + (end_date - start_date) * random.random()).strftime('%Y-%m-%dT%H:%M:%SZ'),
            'text': random.choice(texts),
            'public_metrics': {
                'retweet_count': random.randint(0, 100),
                'reply_count': random.randint(0, 100),
                'like_count': random.randint(0, 100),
                'quote_count': random.randint(0, 100)
            },
            'in_reply_to_user_id': str(random.randint(0, 100)),
            'id': str(random.randint(0, 100)),
            'conversation_id': str(random.randint(0, 100)),
            'lang': 'en'
        }
        tweets.append(tweet)

    users = []
    for i in range(10):
        user = {
            "id": str(random.randint(0, 100)),
            "name": "User " + str(i+1),
            "created_at": (start_date + (end_date - start_date) * random.random()).strftime('%Y-%m-%dT%H:%M:%SZ'),
            "username": "user" + str(i+1)
        }
        users.append(user)

    # Define se deve incluir ou não o campo 'next_token' na resposta
    include_next_token = random.choice([True, False])

    # Retorna a resposta como JSON
    response = {
        'data': tweets,
        'includes': {'users': users}
    }
    if include_next_token:
        response['meta'] = {
            'next_token': '1234567890abcdef'
        }

    response = make_response(jsonify(response))
    response.headers['Content-Type'] = 'application/json'

    return response

if __name__ == "__main__":
  app.run(host='0.0.0.0', port='8080')