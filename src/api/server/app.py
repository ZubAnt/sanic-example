from sanic import Sanic
import logging

from server.application import Application

logging.getLogger().setLevel(logging.ERROR)


app = Sanic()
application = Application()
application.register(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False, access_log=False, workers=1)