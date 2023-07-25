from flask import Flask
from flask_restful import Api

from api.aggregated_api import AggregatedApi


app = Flask(__name__)
api = Api(app)
api.add_resource(AggregatedApi, '/')


app.run(debug=True)



