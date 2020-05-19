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


@app.route('/api/v1/ibaraki')
def get_ibaraki():
    return jsonify(ibaraki)


@app.route('/api/v1/tochigi')
def get_tochigi():
    return jsonify(tochigi)


@app.route('/api/v1/gunma')
def get_gunma():
    return jsonify(gunma)


@app.route('/api/v1/saitama')
def get_saitama():
    return jsonify(saitama)


@app.route('/api/v1/chiba')
def get_chiba():
    return jsonify(chiba)


@app.route('/api/v1/tokyo')
def get_tokyo():
    return jsonify(tokyo)


@app.route('/api/v1/kanagawa')
def get_kanagawa():
    return jsonify(kanagawa)


@app.route('/api/v1/niigata')
def get_niigata():
    return jsonify(niigata)


@app.route('/api/v1/toyama')
def get_toyama():
    return jsonify(toyama)


@app.route('/api/v1/ishikawa')
def get_ishikawa():
    return jsonify(ishikawa)


@app.route('/api/v1/fukui')
def get_fukui():
    return jsonify(fukui)


@app.route('/api/v1/yamanashi')
def get_yamanashi():
    return jsonify(yamanashi)


@app.route('/api/v1/nagano')
def get_nagano():
    return jsonify(nagano)


@app.route('/api/v1/gifu')
def get_gifu():
    return jsonify(gifu)


@app.route('/api/v1/shizuoka')
def get_shizuoka():
    return jsonify(shizuoka)


@app.route('/api/v1/aichi')
def get_aichi():
    return jsonify(aichi)
