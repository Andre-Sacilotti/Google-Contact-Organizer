"""Start module, its only for dev purposes."""
from api.server import application


from api.models.User import User

import fireo


fireo.connection(from_file = "/home/andresacilotti/Downloads/desafio-conecta-d4fbb-firebase-adminsdk-n45a5-99ce66d235.json")

print("Salvando")
User(
    id="aaaaaaaaaa", email="aaaaaaaaaaa",name="aaaaaaaaaaaaaaaaaaaaaa"
).save()
print("salvo")

application.run(debug=False)
