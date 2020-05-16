from flask import Flask, jsonify
from prefectures import *

app = Flask(__name__)


@app.route('/api/v1/hokkaido')
def get_hokkaido():
    return jsonify(hokkaido)


@app.route('/api/v1/aomori')
def get_aomori():
    return jsonify(aomori)


if __name__ == 'main':
    app.run()
