from api import app
from flask import jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from prefectures import *

limiter = Limiter(
    app,
    key_func=get_remote_address,
)

@app.route('/api/v1/japan')
@limiter.limit("3 per minute")
def get_japan():
    return jsonify(japan)


@app.route('/api/v1/hokkaido')
@limiter.limit("3 per minute")
def get_hokkaido():
    return jsonify(hokkaido)


@app.route('/api/v1/aomori')
@limiter.limit("3 per minute")
def get_aomori():
    return jsonify(aomori)


@app.route('/api/v1/iwate')
@limiter.limit("3 per minute")
def get_iwate():
    return jsonify(iwate)


@app.route('/api/v1/miyagi')
@limiter.limit("3 per minute")
def get_miyagi():
    return jsonify(miyagi)


@app.route('/api/v1/akita')
@limiter.limit("3 per minute")
def get_akita():
    return jsonify(akita)


@app.route('/api/v1/yamagata')
@limiter.limit("3 per minute")
def get_yamagata():
    return jsonify(yamagata)


@app.route('/api/v1/fukushima')
@limiter.limit("3 per minute")
def get_fukushima():
    return jsonify(fukushima)


@app.route('/api/v1/ibaraki')
@limiter.limit("3 per minute")
def get_ibaraki():
    return jsonify(ibaraki)


@app.route('/api/v1/tochigi')
@limiter.limit("3 per minute")
def get_tochigi():
    return jsonify(tochigi)


@app.route('/api/v1/gunma')
@limiter.limit("3 per minute")
def get_gunma():
    return jsonify(gunma)


@app.route('/api/v1/saitama')
@limiter.limit("3 per minute")
def get_saitama():
    return jsonify(saitama)


@app.route('/api/v1/chiba')
@limiter.limit("3 per minute")
def get_chiba():
    return jsonify(chiba)


@app.route('/api/v1/tokyo')
@limiter.limit("3 per minute")
def get_tokyo():
    return jsonify(tokyo)


@app.route('/api/v1/kanagawa')
@limiter.limit("3 per minute")
def get_kanagawa():
    return jsonify(kanagawa)


@app.route('/api/v1/niigata')
@limiter.limit("3 per minute")
def get_niigata():
    return jsonify(niigata)


@app.route('/api/v1/toyama')
@limiter.limit("3 per minute")
def get_toyama():
    return jsonify(toyama)


@app.route('/api/v1/ishikawa')
@limiter.limit("3 per minute")
def get_ishikawa():
    return jsonify(ishikawa)


@app.route('/api/v1/fukui')
@limiter.limit("3 per minute")
def get_fukui():
    return jsonify(fukui)


@app.route('/api/v1/yamanashi')
@limiter.limit("3 per minute")
def get_yamanashi():
    return jsonify(yamanashi)


@app.route('/api/v1/nagano')
@limiter.limit("3 per minute")
def get_nagano():
    return jsonify(nagano)


@app.route('/api/v1/gifu')
@limiter.limit("3 per minute")
def get_gifu():
    return jsonify(gifu)


@app.route('/api/v1/shizuoka')
@limiter.limit("3 per minute")
def get_shizuoka():
    return jsonify(shizuoka)


@app.route('/api/v1/aichi')
@limiter.limit("3 per minute")
def get_aichi():
    return jsonify(aichi)


@app.route('/api/v1/mie')
@limiter.limit("3 per minute")
def get_mie():
    return jsonify(mie)


@app.route('/api/v1/shiga')
@limiter.limit("3 per minute")
def get_shiga():
    return jsonify(shiga)


@app.route('/api/v1/kyoto')
@limiter.limit("3 per minute")
def get_kyoto():
    return jsonify(kyoto)


@app.route('/api/v1/osaka')
@limiter.limit("3 per minute")
def get_osaka():
    return jsonify(osaka)


@app.route('/api/v1/hyogo')
@limiter.limit("3 per minute")
def get_hyogo():
    return jsonify(hyogo)


@app.route('/api/v1/nara')
@limiter.limit("3 per minute")
def get_nara():
    return jsonify(nara)


@app.route('/api/v1/wakayama')
@limiter.limit("3 per minute")
def get_wakayama():
    return jsonify(wakayama)


@app.route('/api/v1/tottori')
@limiter.limit("3 per minute")
def get_tottori():
    return jsonify(tottori)


@app.route('/api/v1/shimane')
@limiter.limit("3 per minute")
def get_shimane():
    return jsonify(shimane)


@app.route('/api/v1/okayama')
@limiter.limit("3 per minute")
def get_okayama():
    return jsonify(okayama)


@app.route('/api/v1/hiroshima')
@limiter.limit("3 per minute")
def get_hiroshima():
    return jsonify(hiroshima)


@app.route('/api/v1/yamaguchi')
@limiter.limit("3 per minute")
def get_yamaguchi():
    return jsonify(yamaguchi)


@app.route('/api/v1/tokushima')
@limiter.limit("3 per minute")
def get_tokushima():
    return jsonify(tokushima)


@app.route('/api/v1/kagawa')
@limiter.limit("3 per minute")
def get_kagawa():
    return jsonify(kagawa)


@app.route('/api/v1/ehime')
@limiter.limit("3 per minute")
def get_ehime():
    return jsonify(ehime)


@app.route('/api/v1/kochi')
@limiter.limit("3 per minute")
def get_kochi():
    return jsonify(kochi)


@app.route('/api/v1/fukuoka')
@limiter.limit("3 per minute")
def get_fukuoka():
    return jsonify(fukuoka)


@app.route('/api/v1/saga')
@limiter.limit("3 per minute")
def get_saga():
    return jsonify(saga)


@app.route('/api/v1/nagasaki')
@limiter.limit("3 per minute")
def get_nagasaki():
    return jsonify(nagasaki)


@app.route('/api/v1/kumamoto')
@limiter.limit("3 per minute")
def get_kumamoto():
    return jsonify(kumamoto)


@app.route('/api/v1/oita')
@limiter.limit("3 per minute")
def get_oita():
    return jsonify(oita)


@app.route('/api/v1/miyazaki')
@limiter.limit("3 per minute")
def get_miyazaki():
    return jsonify(miyazaki)


@app.route('/api/v1/kagoshima')
@limiter.limit("3 per minute")
def get_kagoshima():
    return jsonify(kagoshima)


@app.route('/api/v1/okinawa')
@limiter.limit("3 per minute")
def get_okinawa():
    return jsonify(okinawa)


@app.route('/api/v1/all')
@limiter.limit("3 per minute")
def get_all():
    return jsonify(japan, hokkaido, aomori, iwate, miyagi, akita, yamagata, fukushima,
                   ibaraki, tochigi, gunma, saitama, chiba, tokyo, kanagawa, niigata,
                   toyama, ishikawa, fukui, yamanashi, nagano, gifu, shizuoka, aichi,
                   mie, shiga, kyoto, osaka, hyogo, nara, wakayama, tottori, shimane,
                   okayama, hiroshima, yamaguchi, tokushima, kagawa, ehime, kochi,
                   fukuoka, saga, nagasaki, kumamoto, oita, miyazaki, kagoshima, okinawa)


@app.route('/api/v1/iso_code/<int:iso>')
@limiter.limit("3 per minute")
def get_by_iso(iso):
    for prefecture in all_prefectures:
        if iso < 1 or iso > 47:
            return 'Enter number between 1-47'
        if iso == prefecture['iso_code']:
            return jsonify(prefecture)


@app.route('/api/v1/area_rank/<int:area_rank>')
@limiter.limit("3 per minute")
def get_by_area_rank(area_rank):
    for prefecture in all_prefectures:
        if area_rank < 1 or area_rank > 47:
            return 'Enter number between 1-47'
        if area_rank == prefecture['area_rank']:
            return jsonify(prefecture)



@app.route('/api/v1/population_rank/<int:population_rank>')
@limiter.limit("3 per minute")
def get_by_population_rank(population_rank):
    for prefecture in all_prefectures:
        if population_rank < 1 or population_rank > 47:
            return 'Enter number between 1-47'
        if population_rank == prefecture['population_rank']:
            return jsonify(prefecture)


@app.route('/')
@app.route('/api')
@app.route('/api/')
@app.route('/api/v1')
@app.route('/api/v1/')
def show_docs():
    return '<h1><a href="https://japan-api.github.io/docs/">API Documentation</a></h1>'


@app.route('/api/v1/area_rank/')
def show_area_rank_message():
    return '<h1>Specify the area rank number 1-47</h1>'

@app.route('/api/v1/population_rank/')
def show_population_rank_message():
    return '<h1>Specify the population rank number 1-47</h1>'

@app.route('/api/v1/iso_code/')
def show_iso_code_message():
    return '<h1>Specify the iso code number 1-47</h1>'