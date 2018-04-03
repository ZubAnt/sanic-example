from sanic import Sanic
from sanic.request import Request
from sanic.response import json
import logging

app = Sanic()

logging.getLogger().setLevel(logging.INFO)


@app.middleware('request')
async def halt_request(request: Request):
    logging.info(f"request: {request}")


@app.route('/')
async def test(request):
    return json({'hello': 'world'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False, access_log=False)