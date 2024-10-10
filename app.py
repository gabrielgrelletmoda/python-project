import requests
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

def criar_registro_pipefy(dados, pipefy_token, pipefy_api_url):
    query = """
    mutation($tableId: ID!, $title: String!, $fieldsAttributes: [FieldAttributesInput!]!) {
        createTableRecord(input: {table_id: $tableId, title: $title, fields_attributes: $fieldsAttributes}) {
            table_record {
                id
            }
        }
    }
    """

    headers = {
        'Authorization': pipefy_token,
        'Content-Type': 'application/json',
    }

    variables = {
        'tableId': dados.get('table_id'),
        'title': dados.get('title', 'New record'),
        'fieldsAttributes': dados.get('fields_attributes', [])
    }

    response = requests.post(pipefy_api_url, json={'query': query, 'variables': variables}, headers=headers)

    if response.status_code != 200:
        abort(response.status_code, description=response.text)

    return response.json()

@app.route('/registrar', methods=['POST'])
def registrar():
    dados = request.json
    pipefy_token = request.headers.get('PIPEFY_TOKEN')
    pipefy_api_url = request.headers.get('PIPEFY_API_URL')

    if not pipefy_token or not pipefy_api_url:
        abort(400, description="Missing PIPEFY_TOKEN or PIPEFY_API_URL in headers")

    resultado = criar_registro_pipefy(dados, pipefy_token, pipefy_api_url)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)

