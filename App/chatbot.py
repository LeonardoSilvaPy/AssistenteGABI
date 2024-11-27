from flask import Flask, request, jsonify
# importa a classe
from responses.Response import AIBot

# inicia o flask
app = Flask(__name__)
# seta a rota de teste
@app.route('/chatbot/', methods=['POST'])
def response():
    # cria um objeto da classe AIBot
    ai_bot = AIBot()
    # menssage recebe a mensagem enviada pelo usuario
    menssage = request.json.get("message")

    # cria uma variavel que recebe a resposta da class AIBot e passa a variavel de mensagem
    response = ai_bot.invoke(question=menssage)

    # retorna a resposta gerada pelo modelo
    return jsonify({'return': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)