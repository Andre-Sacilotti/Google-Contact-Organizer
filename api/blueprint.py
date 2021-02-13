"""Blueprint module for api endpoints."""
from flask import Blueprint


api_blueprint = Blueprint("api", __name__,)


import api.contacts.contacts_api
