from api import app
from flask import jsonify
from prefectures import *


@app.route('/api/v1/hokkaido')
def get_hokkaido():
    return jsonify(hokkaido)


@app.route('/api/v1/aomori')
def get_aomori():
    return jsonify(aomori)


@app.route('/api/v1/iwate')
def get_iwate():
    return jsonify(iwate)


@app.route('/api/v1/miyagi')
def get_miyagi():
    return jsonify(miyagi)


@app.route('/api/v1/akita')
def get_akita():
    return jsonify(akita)


@app.route('/api/v1/yamagata')
def get_yamagata():
    return jsonify(yamagata)


@app.route('/api/v1/fukushima')
def get_fukushima():
    return jsonify(fukushima)
