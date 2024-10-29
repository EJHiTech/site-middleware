import os
from flask import Flask, request, jsonify
from flask_cors import CORS  # Importa o CORS
import requests
import logging

app = Flask(__name__)
CORS(app)  # Permite acesso de qualquer origem

# Configuração do logging
logging.basicConfig(
    filename='app.log',  # Nome do arquivo de log
    level=logging.DEBUG,  # Nível de log
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato da mensagem
)

# Obtém a chave da API do ClickUp a partir da variável de ambiente
CLICKUP_API_KEY = os.getenv("CLICKUP_API_KEY")
CLICKUP_API_BASE_URL = "https://api.clickup.com/api/v2/list/901305397122/task"

@app.route('/publish-task', methods=['POST', 'GET', 'PUT', 'DELETE'])
def proxy_request():
    logging.debug('TESTE1: A função proxy_request foi chamada.')

    # Headers para a requisição ao ClickUp
    headers = {
        "Authorization": CLICKUP_API_KEY,
        "Content-Type": "application/json"
    }
    
    logging.debug(f'HEADERS: {headers}')
    logging.debug(f'Key: {CLICKUP_API_KEY}')

    data = request.get_json() if request.is_json else None
    params = request.args
    
    try:
        clickup_url = f"{CLICKUP_API_BASE_URL}"
        clickup_response = requests.request(
            method=request.method,
            url=clickup_url,
            headers=headers,
            json=data,
            params=params
        )
        logging.debug(f'Erro ClickUp: {clickup_response.json()}')
        return jsonify(clickup_response.json()), clickup_response.status_code
    except Exception as e:
        logging.error(f'Erro: {str(e)}')
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def test_route():
    print('\n\nTESTE2 - Rota de teste acessada\n\n')
    return jsonify({"status": "OK"}), 200

if __name__ == '__main__':
    print('\n\n\nTESTE0\n\n\n')
    app.run(host='0.0.0.0', port=5000, debug=True)