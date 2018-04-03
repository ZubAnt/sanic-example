from flask import Flask
from injector import inject, singleton

from server.blueprints.default_blueprint import DefaultBlueprint
from server.ioc import ioc


class Application(object):

    @inject
    def __init__(self) -> None:
        self._default = ioc.get(DefaultBlueprint, scope=singleton).blueprint

    def register(self, app: Flask) -> None:
        app.register_blueprint(self._default, url_prefix='/default')

