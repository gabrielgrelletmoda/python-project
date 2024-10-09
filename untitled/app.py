import requests
from flask import Flask, request, jsonify

app = Flask(__name__)



def criar_registro_pipefy(dados):
    query = """
    mutation {
      createCard(input: {
        pipe_id: "ID_DO_PIPE"
        title: "%s"
        fields_attributes: [
          {
            field_id: "ID_DO_CAMPO_NOME"
            field_value: "%s"
          },
          {
            field_id: "ID_DO_CAMPO_EMAIL"
            field_value: "%s"
          }
        ]
      }) {
        card {
          id
          title
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
def registrar():
    dados = request.json
    resultado = criar_registro_pipefy(dados)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
