from api import app
from flask import jsonify
from prefectures import *


@app.route('/api/v1/japan')
def get_japan():
    return jsonify(japan)


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


@app.route('/api/v1/mie')
def get_mie():
    return jsonify(mie)


@app.route('/api/v1/shiga')
def get_shiga():
    return jsonify(shiga)


@app.route('/api/v1/kyoto')
def get_kyoto():
    return jsonify(kyoto)


@app.route('/api/v1/osaka')
def get_osaka():
    return jsonify(osaka)


@app.route('/api/v1/hyogo')
def get_hyogo():
    return jsonify(hyogo)


@app.route('/api/v1/nara')
def get_nara():
    return jsonify(nara)


@app.route('/api/v1/wakayama')
def get_wakayama():
    return jsonify(wakayama)


@app.route('/api/v1/tottori')
def get_tottori():
    return jsonify(tottori)


@app.route('/api/v1/shimane')
def get_shimane():
    return jsonify(shimane)


@app.route('/api/v1/okayama')
def get_okayama():
    return jsonify(okayama)


@app.route('/api/v1/hiroshima')
def get_hiroshima():
    return jsonify(hiroshima)


@app.route('/api/v1/yamaguchi')
def get_yamaguchi():
    return jsonify(yamaguchi)


@app.route('/api/v1/tokushima')
def get_tokushima():
    return jsonify(tokushima)


@app.route('/api/v1/kagawa')
def get_kagawa():
    return jsonify(kagawa)


@app.route('/api/v1/ehime')
def get_ehime():
    return jsonify(ehime)


@app.route('/api/v1/kochi')
def get_kochi():
    return jsonify(kochi)


@app.route('/api/v1/fukuoka')
def get_fukuoka():
    return jsonify(fukuoka)


@app.route('/api/v1/saga')
def get_saga():
    return jsonify(saga)


@app.route('/api/v1/nagasaki')
def get_nagasaki():
    return jsonify(nagasaki)


@app.route('/api/v1/kumamoto')
def get_kumamoto():
    return jsonify(kumamoto)


@app.route('/api/v1/oita')
def get_oita():
    return jsonify(oita)


@app.route('/api/v1/miyazaki')
def get_miyazaki():
    return jsonify(miyazaki)


@app.route('/api/v1/kagoshima')
def get_kagoshima():
    return jsonify(kagoshima)


@app.route('/api/v1/okinawa')
def get_okinawa():
    return jsonify(okinawa)


@app.route('/api/v1/all')
def get_all():
    return jsonify(japan, hokkaido, aomori, iwate, miyagi, akita, yamagata, fukushima,
                   ibaraki, tochigi, gunma, saitama, chiba, tokyo, kanagawa, niigata,
                   toyama, ishikawa, fukui, yamanashi, nagano, gifu, shizuoka, aichi,
                   mie, shiga, kyoto, osaka, hyogo, nara, wakayama, tottori, shimane,
                   okayama, hiroshima, yamaguchi, tokushima, kagawa, ehime, kochi,
                   fukuoka, saga, nagasaki, kumamoto, oita, miyazaki, kagoshima, okinawa)


@app.route('/api/v1/iso_code/<int:iso>')
def get_by_iso(iso):
    for prefecture in all_prefectures:
        if iso == prefecture['iso_code']:
            return jsonify(prefecture)


@app.route('/api/v1/area_rank/<int:area_rank>')
def get_by_area_rank(area_rank):
    for prefecture in all_prefectures:
        if area_rank == prefecture['area_rank']:
            return jsonify(prefecture)


@app.route('/api/v1/population_rank/<int:population_rank>')
def get_by_population_rank(population_rank):
    for prefecture in all_prefectures:
        if population_rank == prefecture['population_rank']:
            return jsonify(prefecture)


@app.route('/')
@app.route('/api')
@app.route('/api/')
@app.route('/api/v1')
@app.route('/api/v1/')
def show_docs():
    return '<h1><a href="https://github.com/japan-api/docs">API Documentation</a></h1>'


@app.route('/api/v1/area_rank/')
def show_area_rank_message():
    return '<h1>Specify the area rank number 1-47</h1>'

@app.route('/api/v1/population_rank/')
def show_population_rank_message():
    return '<h1>Specify the population rank number 1-47</h1>'

@app.route('/api/v1/iso_code/')
def show_iso_code_message():
    return '<h1>Specify the iso code number 1-47</h1>'