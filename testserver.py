"""Start module, its only for dev purposes."""
from api.server import application
import os

from api.models.User import User
import fireo
from firebase_admin import credentials, initialize_app

os.environ["DEBUG"] = "true"

cred = None

if os.getenv("DEBUG") == 'true':
    cred = credentials.Certificate("/auth/desafio-conecta-d4fbb-firebase-adminsdk-n45a5-99ce66d235.json")
else:
    cred = credentials.Certificate()
initialize_app(cred, {'storageBucket': 'desafio-conecta-d4fbb.appspot.com'})




fireo.connection(
    from_file="/auth/desafio-conecta-d4fbb-firebase-adminsdk-n45a5-99ce66d235.json"
)

application.run(debug=False, host="0.0.0.0")
