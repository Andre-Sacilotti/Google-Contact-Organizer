"""Module for contact api."""
import requests
import json
from flask import request
from api.server import api_blueprint
from flask_restplus import Resource, reqparse, fields

contact_namespace = api_blueprint.namespace(
    "contact", description="Read and manage Contacts"
)


@contact_namespace.route("/")
class ContactApi(Resource):
    """Restful API to deal with contacts."""

    @contact_namespace.header(
        "authorization-code",
        "OAuth2 Access Token given by google api.",
        required=True,
    )
    @contact_namespace.doc(responses={200: "OK", 401: "Invalid Token"},)
    def get(self):
        """Get method that return a dictionary with useful informations."""
        print(request.headers)
        token = request.get_json(force=True)["token"]

        authorization_header = {"Authorization": "Bearer %s" % token}

        r = requests.get(
            "https://people.googleapis.com/v1/people/me/connections?personFields=names,emailAddresses,photos",
            headers=authorization_header,
        )

        json_data = json.loads(r.text)

        if json_data.get("error", None) is not None:
            if json_data["error"]["code"] == 401:
                return {"error": "Invalid authentication credential"}, 401
            else:
                return json_data, 402
        else:

            return json_data, 200
