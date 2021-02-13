from api.server import api_blueprint
from flask_restplus import Resource


@api_blueprint.route("/user")
class UserApi(Resource):
    def get(self):
        return "aaa"
