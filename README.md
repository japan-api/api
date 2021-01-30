# Japan API 🎌
LINK FOR API - https://japan-api.ninja/api/v1/ <br>
A Complete REST API about Prefectures of Japan using Python 3 and Flask<br>
Currently there are <b>47</b> (All) prefectures and <b>20</b> fields (May add more)<br>
Most of the data is taken from the <a href="https://en.wikipedia.org/wiki/Prefectures_of_Japan">Wikipedia</a>,
<a href="https://www.tofugu.com/japan/japanese-food-by-prefecture/">Food data</a>, <a href="http://www.fukushima.climatemps.com">Climate data</a><br>
If you have noticed some mistakes or bugs, or maybe you have any suggestions please create an issue.

# Preview 🔍
<img src="https://i.imgur.com/mCct5TL.jpg" width="430">

# Docs 📘
Site with docs is here https://japan-api.github.io/docs/ <br>
You can use this API to get detailed information aboout Japan <br>
Japan API has only GET request method<br>
Japan API has 54 endpoints <br> 
* All Prefectures of Japan (47)
* Japan itself 
* All prefectures (including Japan)
* Find By ISO code, By population and area rank (Among all prefectures)
* Random Prefecture and Random Fact about Japan

```area_rank, population_rank``` - stands for local Japanese rank between all prefectures (47) <br>
```area_rank, population_rank, density_rank``` In Japan endpoint means Worldwide rank

# List of endpoints 📜
/api/v1/all <br>
/api/v1/iso/<int:prefecture_iso> - Find by ISO code, list of codes | link > <a href="https://en.wikipedia.org/wiki/ISO_3166-2:JP">JP ISO codes</a> <br>
/api/v1/population_rank/<int:population_rank> - Find by population rank (Among all prefectures)<br>
/api/v1/area_rank/<int:area_rank> - Find by area rank (Among all prefectures)<br>
/api/v1/random_prefecture <br>
/api/v1/random_fact <br>
/api/v1/japan  <br>
/api/v1/hokkaido <br>
/api/v1/aomori <br>
/api/v1/iwate <br>
/api/v1/miyagi <br>
/api/v1/akita <br>
/api/v1/yamagata <br>
/api/v1/fukushima <br>
/api/v1/ibaraki <br>
/api/v1/tochigi <br>
/api/v1/gunma <br>
/api/v1/saitama <br>
/api/v1/chiba <br>
/api/v1/tokyo <br>
/api/v1/kanagawa <br>
/api/v1/niigata <br>
/api/v1/toyama <br>
/api/v1/ishikawa <br>
/api/v1/fukui <br>
/api/v1/yamanashi <br>
/api/v1/nagano <br>
/api/v1/gifu <br>
/api/v1/shizuoka <br>
/api/v1/aichi <br>
/api/v1/mie <br>
/api/v1/shiga <br>
/api/v1/kyoto <br>
/api/v1/osaka <br>
/api/v1/hyogo <br>
/api/v1/nara <br>
/api/v1/wakayama <br>
/api/v1/tottori <br>
/api/v1/shimane <br>
/api/v1/okayama <br>
/api/v1/hiroshima <br>
/api/v1/yamaguchi <br>
/api/v1/tokushima <br>
/api/v1/kagawa <br>
/api/v1/ehime <br>
/api/v1/kochi <br>
/api/v1/fukuoka<br>
/api/v1/saga<br>
/api/v1/nagasaki<br>
/api/v1/kumamoto<br>
/api/v1/oita<br>
/api/v1/miyazaki<br>
/api/v1/kagoshima<br>
/api/v1/okinawa<br>

# Usage 👩‍💻👨‍💻
Just fetch data from the api using GET method

# Quick Start 🚀
```git clone https://github.com/japan-api/api``` <br>
```cd api```<br>
```pip install requirements.txt OR python -m pip install -r requirements.txt``` <br>
```cd tests```<br>
```python test_prefectures.py```<br>
```cd ../api``` <br>
```set FLASK_APP=api.py``` <br>
```python -m flask run```

# Contributing 🤝
Contributions, issues and feature requests are welcome! 👍 <br>
Feel free to check open issues.

# ToDo 
- Searach for prefectures by the island (Honshu, Kyushu Shikoku, Hokkaido)

# What I Learned 🧠
* Flask basics: routing, serving
* JSON

# License 📑 
(c) 2021 Ilya Revenko. [MIT License](https://tldrlegal.com/license/mit-license)
