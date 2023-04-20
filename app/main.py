# Importing necessary modules
from flask import Flask, request, make_response, jsonify, render_template
from views.utils import gera_tweets, filtrar_por_regiao, carrega_dados

# Creating Flask application instance
app = Flask(__name__)

# Configuring Flask application to not sort JSON keys
app.config['JSON_SORT_KEYS'] = False

# Home page route
@app.route('/')
def home():
    """
    Renders the home page
    """
    return render_template('index.html')

# Hello World page route
@app.route('/hello-world')
def hello_world():
    """
    Renders the hello world page
    """
    return render_template('hello-world.html')

# Products API route
@app.route("/produtos")
def produtos():
    """
    API endpoint to filter products by region and year
    """
    # Extracting query parameters from request
    regiao = request.args.get("regiao", default=None, type=str)
    ano = request.args.get("ano", default=None, type=int)

    # Filtering data by region and year
    dados_filtrados = filtrar_por_regiao(carrega_dados(), regiao, ano)

    return jsonify(dados_filtrados)

# Search recent tweets API route
@app.route('/2/tweets/search/recent')
def search_recent_tweets():
    """
    API endpoint to search recent tweets based on query, start time and end time
    """
    # Extracting query parameters from request
    query = request.args.get('query')
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')

    # Generating tweets based on query, start time and end time
    tweets = gera_tweets(query, start_time, end_time)

    # Creating response
    response = make_response(jsonify(tweets))
    response.headers['Content-Type'] = 'application/json'

    return response

if __name__ == "__main__":
    # Starting the Flask application
    app.run(host='0.0.0.0', port='8080')
