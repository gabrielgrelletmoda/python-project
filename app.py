import requests
from flask import Flask, request, jsonify

app = Flask(__name__)



def criar_registro_pipefy(dados, PIPEFY_TOKEN=None, PIPEFY_API_URL=None):
    query = """
    mutation {
  createTableRecord(input: {table_id: ID, title: "New record", fields_attributes: {field_id: "text", field_value: "New value for this record field"}}) {
    table_record {
      id
    }
  }
}
    """ % (dados['nome'], dados['nome'], dados['email'])

    headers = {
        'Authorization': PIPEFY_TOKEN,
        'Content-Type': 'application/json',
    }

    response = requests.post(PIPEFY_API_URL, json={'query': query}, headers=headers)
    return response.json()

@app.route('/registrar', methods=['POST'])
def registrar(PIPEFY_TOKEN=None, ):
    dados = request.json
    resultado = criar_registro_pipefy(dados, PIPEFY_TOKEN, PIPEFY_API_URL)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
