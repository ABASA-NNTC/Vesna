from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import werkzeug
import os
import  take_geojson
import clip

app = Flask(__name__)
api = Api(app)


class Geos(Resource):
    def get(self):
        file_js = request.files['filejson']
        print(request.args.get('filejson'))
        print(request.data)
        print(request.date)
        print(request.content_type)
        print(file_js.content_type)

    def post(self):
        file = request.files['filejson']
        file.save(os.path.join('geojsons', file.filename))
        return {}

api.add_resource(Geos, '/geo')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

