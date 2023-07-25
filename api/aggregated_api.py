
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
        return {'hello': 'world'}


def calculate_average(responses):
    pass
