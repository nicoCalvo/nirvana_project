import pytest

from aiohttp import web
import asyncio
import aiohttp
from aioresponses import aioresponses

from api_internal import API_URLS

@pytest.fixture
async def mocked_server(aiohttp_server):
    async def handler(request: web.Request) -> web.Response:
        
        return web.json_response(
            {
                "status": "ok",
                "data": {
                    "id": 1,
                    "title": "test title",
                    "text": "test text",
                    "owner": "test_user",
                    "editor": "test_user",
                },
            }
        )

    app = web.Application()
    import pdb; pdb.set_trace()
    app.add_routes([web.get('', handler)])
    server = await aiohttp_server(app)



@pytest.fixture
def mocked_response():
    with aioresponses() as m:
        yield m
