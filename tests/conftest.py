import pytest

from aioresponses import aioresponses
from flask import Flask
from flask_restful import Api


from api import AggregatedApi

@pytest.fixture
def mocked_response():
    with aioresponses() as m:
        yield m

@pytest.fixture
def app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(AggregatedApi, '/')
    return app




@pytest.fixture
def client(app):
    """A Flask test client. An instance of :class:`flask.testing.TestClient`
    by default.
    """
    with app.test_client() as client:
        yield client