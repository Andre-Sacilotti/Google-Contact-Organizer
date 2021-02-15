"""Start module, its only for dev purposes."""
from api.server import app
from api.models.User import User
import fireo
from firebase_admin import credentials, initialize_app
import os


initialize_app(options={'storageBucket': 'desafio-conecta-d4fbb.appspot.com'})


# fireo.connection(from_file="./desafio-conecta-d4fbb-firebase-adminsdk-n45a5-99ce66d235.json")
