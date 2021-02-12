from api.blueprint import api_blueprint


@api_blueprint.route("/teste")
def teste():
    return "aaaaaaaa"