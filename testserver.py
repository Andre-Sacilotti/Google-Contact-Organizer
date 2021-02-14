"""Start module, its only for dev purposes."""
from api.server import application


from api.models.User import User

import fireo

fireo.connection(from_file = "/auth/desafio-conecta-d4fbb-firebase-adminsdk-n45a5-99ce66d235.json")

application.run(debug=False, host='0.0.0.0')
