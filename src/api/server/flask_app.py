from flask import Flask
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=False)