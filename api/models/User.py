"""User Model, stores id, name and contacts."""
from fireo.fields import TextField, ListField, IDField
from fireo.models import Model


class User(Model):
    """User Class Model, extending from ```fireo.models.Model``` package.

    Attributes
    ----------
    id : str
        User unique id composed by subject id given by google auth.
    name : str
        User display name.
    contacts : list
        List with contacts objects.
    email : str
        Profile email.

    """
    id = IDField()
    name = TextField()
    contacts = ListField()
    email = TextField()
