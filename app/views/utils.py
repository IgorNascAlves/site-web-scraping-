# Importação de módulos
import random
from json import load
from datetime import datetime


def carrega_dados():
    """
    Carrega dados do arquivo JSON de um diretório específico.
    :return: retorna os dados em formato de dicionário
    """
    with open("dados/dados_ecomerce.json", encoding='utf-8') as f:
        dados = load(f)
    return dados


def filtrar_por_regiao(dados, regiao=None, ano=None):
    """
    Filtra dados de compras por região e ano.
    :param dados: dados em formato de dicionário
    :param regiao: região a ser filtrada, aceita valores: 'norte', 'nordeste', 'centro-oeste', 'sudeste' ou 'sul'
    :param ano: ano a ser filtrado
    :return: retorna os dados filtrados em formato de lista
    """

    # Cria um dicionário que define os critérios de cada região
    criterios_regioes = {
        'norte': ['AC', 'AM', 'AP', 'PA', 'RO', 'RR', 'TO'],
        'nordeste': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
        'centro-oeste': ['DF', 'GO', 'MT', 'MS'],
        'sudeste': ['ES', 'MG', 'RJ', 'SP'],
        'sul': ['PR', 'RS', 'SC']
    }

    # Inicializa uma lista vazia que armazenará os dados filtrados
    dados_filtrados = []

    # Percorre cada item dos dados
    for d in dados:
        estado = d.get('Local da compra')
        data_compra = d.get('Data da Compra')

        # Verifica se o estado está na região especificada ou se nenhuma região foi especificada
        # Verifica se a data da compra está no ano especificado ou se nenhum ano foi especificado
        if (not regiao or estado and estado.upper() in criterios_regioes.get(regiao, [])) and \
                (not ano or data_compra and datetime.strptime(data_compra, '%d/%m/%Y').year == ano):
            dados_filtrados.append(d)

    # Retorna a lista de dados filtrados
    return dados_filtrados


def gera_tweets(query, start_time, end_time):
    # Converte as datas para o formato correto
    format_string = '%Y-%m-%dT%H:%M:%S.%f%z'
    start_date = datetime.strptime(start_time, format_string)
    end_date = datetime.strptime(end_time, format_string)

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
            'created_at': (start_date + (end_date - start_date) * random.random()).strftime(format_string),
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

    # Gera uma lista de usuários fictícios
    users = []
    for i in range(10):
        user = {
            "id": str(random.randint(0, 100)),
            "name": "User " + str(i+1),
            "created_at": (start_date + (end_date - start_date) * random.random()).strftime(format_string),
            "username": "user" + str(i+1)
        }
        users.append(user)

    # Define se deve incluir ou não o campo 'next_token' na resposta
    include_next_token = random.choice([True, False])

    # Monta a resposta com os tweets e usuários fictícios gerados
    response = {
        'data': tweets,
        'includes': {'users': users}
    }
    if include_next_token:
        response['meta'] = {
            'next_token': '1234567890abcdef'
        }

    return response
