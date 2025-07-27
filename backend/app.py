from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from utils.vector_calculus import compute

app = Flask(__name__, template_folder='../templates')
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')
    # return "Welcome to the Vector Calculus API"

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    operation = data['operation']
    expression = data['expression']
    result = compute(operation, expression)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, port=5050)