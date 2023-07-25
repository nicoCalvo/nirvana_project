
import pytest
from api_internal import (
    API_URLS,
    deducible_api_caller,
    DeductibleApiError,
    start_loop
)


def test_internal_api_valid_response(mocked_response):
    start_loop()
    valid_response = {'deductible': 1000, 'stop_loss': 10000, 'oop_max': 5000}
    for api_url in API_URLS:
        mocked_response.get(f"{api_url}?member_id=1", status=200, payload=valid_response)
    res = deducible_api_caller(1)
    assert len(res) == 3
    assert res[0] == res[1] == res[2] == valid_response


def test_internal_api_valid_response(mocked_response):
    start_loop()
    for api_url in API_URLS:
        mocked_response.get(f"{api_url}?member_id=1", status=500)
    with pytest.raises(DeductibleApiError) as err:
        res = deducible_api_caller(1)
