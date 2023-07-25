
import logging

from flask import request
from flask_restful import (
    abort,
    Resource
)

from api_internal import (
    DeductibleApiError,
    deducible_api_caller,
    start_loop
)


logger = logging.getLogger(__name__)


class AggregatedApi(Resource):
    MEMBER_ID = 'member_id'

    def __init__(self, *args, **kwargs):
        super(AggregatedApi, self).__init__(*args, **kwargs)
        start_loop()

    def get(self):
        member_ids = request.args.getlist(self.MEMBER_ID)
        if len(member_ids) == 0 or len(member_ids) > 1:
            abort(409, message="invalid member_id - only 1 allowed")
        try:
            responses = deducible_api_caller(member_ids[0])
        except DeductibleApiError:
            logger.exception("Invalid response from internal APIs")
            abort(500, message="Cannot process the request")

        avg_responses = calculate_average(responses)
        return avg_responses


def calculate_average(responses):
    avg_api_responses = {'deductible': 0, 'stop_loss': 0, 'oop_max': 0}
    for resp in responses:
        avg_api_responses = {
            key: resp[key] + avg_api_responses[key]  for key in resp
        }
    avg_api_responses ={
        key: int(avg_api_responses[key] / len(responses))
        for key in avg_api_responses
    }
    return avg_api_responses


