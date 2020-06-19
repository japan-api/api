from flask import Flask

app = Flask(__name__)

from routes import *

if __name__ == 'main':
    app.run()
