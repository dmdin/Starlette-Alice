import json
import logging

import uvicorn
from alice_sdk import AliceRequest
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

from logic import do_something


def preprocess_request(request):
    return json.loads(request)


async def main(request):
    request = AliceRequest(await request.body())
    response = request.create_response()
    response.set_message(do_something())
    logging.info(request)
    return JSONResponse(response.body())


routes = [
    Route('/', endpoint=main, methods=['POST'])
]

app = Starlette(routes=routes)

if __name__ == '__main__':
    uvicorn.run('app:app', reload=True)
