from flask import Flask
from flask_cors import CORS
from flask_restplus import Resource, Api


application = Flask(__name__)
cors = CORS(application, resources={r"/*": {"origins": "*"}})


api_blueprint = Api(
    application,
    prefix="/api",
    version="0.1",
    title="Super OrgContact API",
    description="Deal with some google people api requests",
)


import api.user.user_api
import api.contacts.contacts_api
