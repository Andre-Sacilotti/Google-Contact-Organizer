"""User Model, stores id, name and contacts."""
from fireo.fields import TextField, ListField
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
    photo_url : str
        Profile photo url.

    """

    id = TextField(primary_key=True)
    name = TextField()
    contacts = ListField()
    photo_url = TextField()
