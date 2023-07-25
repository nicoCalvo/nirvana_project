from unittest import mock
from mock import patch
import api


@patch('api.aggregated_api.deducible_api_caller',
       return_value=[
        {'deductible': 1000, 'stop_loss': 10000, 'oop_max': 5000},
        {'deductible': 1200, 'stop_loss': 13000, 'oop_max': 6000},
        {'deductible': 1000, 'stop_loss': 10000, 'oop_max': 6000}]
    )
def test_api(mocker_deducible, client):
    
    response = client.get('/?member_id=1')
    assert mocker_deducible.called
    assert response.status_code == 200
    assert response.json == {'deductible': 1066, 'stop_loss': 11000, 'oop_max': 5666}
