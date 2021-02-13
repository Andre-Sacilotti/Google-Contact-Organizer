from api.blueprint import api_blueprint
from flask import request
import requests
import json


@api_blueprint.route("/teste", methods=["POST"])
def teste():
    data = request.data
    token = request.form["token"]

    authorization_header = {"Authorization": "Bearer %s" % token}

    r = requests.get(
        "https://people.googleapis.com/v1/people/me/connections?personFields=names,emailAddresses,photos",
        headers=authorization_header,
    )

    json_data = json.loads(r.text)
    return json_data, 200
