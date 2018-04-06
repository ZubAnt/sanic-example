import sys

import sanic
from sanic import Sanic
import logging

from server.application import Application
from sanic.log import access_logger



LOGGING_CONFIG_DEFAULTS = dict(
    version=1,
    disable_existing_loggers=False,

    loggers={
        "root": {
            "level": "INFO",
            "handlers": ["console"]
        },
        "sanic.error": {
            "level": "INFO",
            "handlers": ["error_console"],
            "propagate": True,
            "qualname": "sanic.error"
        },

        "sanic.access": {
            "level": "ERROR",
            "handlers": ["access_console"],
            "propagate": True,
            "qualname": "sanic.access"
        }
    },
    handlers={
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": sys.stdout
        },
        "error_console": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": sys.stderr
        },
        "access_console": {
            "class": "logging.StreamHandler",
            "formatter": "access",
            "stream": sys.stdout
        },
    },
    formatters={
        "generic": {
            "format": "%(asctime)s [%(process)d] [%(levelname)s] %(message)s",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter"
        },
        "access": {
            "format": "%(asctime)s - (%(name)s)[%(levelname)s][%(host)s]: " +
                      "%(request)s %(message)s %(status)d %(byte)d",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter"
        },
    }
)


# logging.getLogger('sanic.access').setLevel(logging.ERROR)
# log_config = logging.basicConfig(level=logging.ERROR)
# sanic.log.access_logger.setLevel(level=logging.ERROR)

# logging.getLogger('sanic.access').setLevel(logging.ERROR)

app = Sanic('test', log_config=LOGGING_CONFIG_DEFAULTS)
logging.error('the matrix!')

application = Application()
application.register(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)


