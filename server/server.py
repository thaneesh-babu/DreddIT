import json
from django.shortcuts import render

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/search', methods=['POST'])
def search():
    output = request.get_json()
    print(output)