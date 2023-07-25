
from concurrent.futures._base import TimeoutError
import logging
from threading import Thread

import aiohttp
import asyncio
from cerberus import Validator


loop = asyncio.new_event_loop()
logger = logging.getLogger(__name__)


API_URLS = [
    'https://api1.com',
    'https://api2.com',
    'https://api3.com'
]
SCHEMA = schema = {
    'deductible': {'type': 'integer', 'required': True},
    'stop_loss': {'type': 'integer', 'required': True},
    'oop_max': {'type': 'integer', 'required': True},
}
TIMEOUT = 10


validator = Validator(SCHEMA)

async def call_api(url):
     logger.info(f"Calling {url}")
     async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            json_response = await response.json()
        return json_response

async def api_call(urls):
    coros = [call_api(url) for url in urls]
    res = await asyncio.gather(*coros, return_exceptions=True)
    return res


def event_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def start_loop():
    t = Thread(target=event_loop, args=(loop,))
    t.daemon = True
    t.start()


class DeductibleApiError(Exception): pass
    

def deducible_api_caller(member_id):
    urls = [f"{api_url}?member_id={member_id}" for api_url in API_URLS]
    try:
        call = asyncio.run_coroutine_threadsafe(api_call(urls), loop)
        responses = call.result(10)
    except TimeoutError as e:
        logger.exception("Unable to fetch API results")
        raise DeductibleApiError() from e
    try:
        assert all(validator.validate(response, SCHEMA)for response in responses)
    except:
        logger.exception(f"Invalid responses - schema unmatch: {responses}")
        raise DeductibleApiError("Invalid Response")
    return responses
