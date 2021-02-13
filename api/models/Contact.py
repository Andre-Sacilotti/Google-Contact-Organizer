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

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "photo_url": self.photo_url,
            "email": self.email,
        }

    @staticmethod
    def dict_to_object(data):
        return Contact(
            id=data["id"],
            name=data["name"],
            photo_url=data["photo_url"],
            email=data["email"],
        )

    @staticmethod
    def multiples_json_contacts_to_objects(json):

        connections = json["connections"]

        data = {"contacts": []}

        for connection in connections:
            new_contact = Contact(
                id=connection["resourceName"].split("/")[1],
                name=connection["names"][0]["displayName"],
                photo_url=connection["photos"][0]["url"],
                email=connection["emailAddresses"][0]["url"],
            )

            data["contacts"].append(new_contact.to_dict())
