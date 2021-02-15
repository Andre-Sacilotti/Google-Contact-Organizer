from flask import Flask
from flask_cors import CORS
from flask_restplus import Resource, Api
import os

application = Flask(__name__)

api_blueprint = Api(
    application,
    prefix="/api",
    version="0.1",
    title="Super OrgContact API",
    description="Deal with some google people api requests",
)

CORS(application, resources={r"/*": {"origins": "*"}})


import api.user.user_api
import api.contacts.contacts_api
import api.reports.reports_api
