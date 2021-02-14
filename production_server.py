"""Start module, its only for dev purposes."""
from api.server import application
from api.models.User import User
import fireo

fireo.connection()
