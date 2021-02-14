"""User Model, stores id, name and contacts."""
from fireo.fields import TextField, MapField, IDField
from fireo.models import Model


class User(Model):
    """User Class Model, extending from ```fireo.models.Model``` package.

    Attributes
    ----------
    id : str
        User unique id composed by subject id given by google auth.
    name : str
        User display name.
    contacts_statistics : dict
        dictionary containg the statistics about contacts, in other words,
        contacts per domain, contacts per City Adresss, contacts per organization

    """
    id = IDField()
    name = TextField()
    contacts_statistics = MapField()
