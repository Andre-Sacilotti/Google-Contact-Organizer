"""Start module, its only for dev purposes."""

from flask import Flask
from flask_cors import CORS
from api.blueprint import api_blueprint

application = Flask(__name__)
CORS(application)

application.register_blueprint(api_blueprint, url_prefix="/api")

application.run()