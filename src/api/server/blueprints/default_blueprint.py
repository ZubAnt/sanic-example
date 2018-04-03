from injector import inject, singleton
from sanic import Blueprint
from sanic.request import Request

from server.blueprints.base_blueprint import BaseBlueprint


@singleton
class DefaultBlueprint(BaseBlueprint):

    @inject
    def __init__(self) -> None:
        super().__init__()

    @property
    def _name(self) -> str:
        return 'default'

    def _create_blueprint(self) -> Blueprint:
        blueprint = Blueprint(self._name, __name__)

        @blueprint.route('/', methods=['GET'])
        def _default(request: Request):
            return self._return_msg('default')

        return blueprint
