"""Contact Model. Stores email, photo url and name."""
from fireo.models import Model
from fireo.fields import TextField


class Contact(Model):
    """Contact Class model, extending from fireo.models.Model package.

    Attributes
    ----------
    id : str
        Unique id given by google in resourceName.
    name : str
        Contact name, given in names > displayName
    photo_url : str
        Url from profile photo, can be found in photos > url from google json
    email : str
        Contact email, given in emailAddresses > value

    """

    id = TextField(primary_key=True)
    name = TextField()
    photo_url = TextField()
    email = TextField()

    def save(*args, **kwargs):
        ...
