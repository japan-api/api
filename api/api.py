from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Hokkaido(Resource):
    def get(self):
        return {'name': 'Hokkaido'}  # Will be replaced with real data in next commit


api.add_resource(Hokkaido, '/hokkaido')

if __name__ == 'main':
    app.run()
