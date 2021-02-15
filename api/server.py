from flask import Flask, Blueprint, request, send_file, url_for
from flask_cors import CORS
from flask_restplus import Api, Namespace, Resource, fields
import os

app = Flask(__name__)

if os.getenv("DEBUG") == 'true':
    ...
else:
    @property
    def specs_url(self):
        return url_for(self.endpoint('specs'), _external=True, _scheme='https')
 
    Api.specs_url = specs_url

api_blueprint = Api(
    app,
    prefix="/api",
    version="0.1",
    title="Super OrgContact API",
    description="Deal with some google people api requests",
)

CORS(app, resources={r"/*": {"origins": "*"}})


import api.user.user_api
import api.contacts.contacts_api
import api.reports.reports_api
