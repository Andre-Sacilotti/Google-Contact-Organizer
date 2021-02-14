"""Contact Model. Stores email, photo url and name."""
from fireo.models import Model
from fireo.fields import TextField
import logging
from datetime import datetime


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
        """Convert an Contact objecto to a dictionary.

        The dict contains the following structure:
        {
            "id": self.id,
            "name": self.name,
            "photo_url": self.photo_url,
            "email": self.email,
        }

        Returns
        -------
        Dict
            Dictionary containing all the informations about a Contact

        """
        return {
            "id": self.id,
            "name": self.name,
            "photo_url": self.photo_url,
            "email": self.email,
        }

    @staticmethod
    def dict_to_object(data):
        """Convert a given dictionary to a Contact Object.

        The dict must contains the following structure:
        {
            "id": self.id,
            "name": self.name,
            "photo_url": self.photo_url,
            "email": self.email,
        }

        Parameters
        ----------
        data : Contact
            Contact object to converto a dict structure

        """
        return Contact(
            id=data["id"],
            name=data["name"],
            photo_url=data["photo_url"],
            email=data["email"],
        )

    @staticmethod
    def multiples_json_contacts_to_objects(json):
        """Convert the request from google people api into a useful list.

        This methods create a list containing all the contacts got from api,
        storing only id, name, photo_url and email.

        Parameters
        ----------
        json : dict
            dictionary returned from Google People Api, connections GET.

        Returns
        -------
        List
            a list containing contacts objects, in the following way:
            [
                Contact(id="123", name="test", photo_url="...", email="@..."),
                Contact(id="345", name="name", photo_url="...", email="@..."),
                Contact(id="456", name="name_t", photo_url="...", email="@...")
            ]

        """
        connections = json["connections"]

        data = {"contacts": []}

        for connection in connections:
            try:
                new_contact = Contact(
                    id=connection["resourceName"].split("/")[1],
                    name=connection.get(
                        "names", [{"displayName": "Missin Name"}]
                    )[0]["displayName"],
                    photo_url=connection.get("photos", [{"url": ""}])[0][
                        "url"
                    ],
                    email=connection["emailAddresses"][0]["value"],
                )
                data["contacts"].append(new_contact.to_dict())
            except KeyError as e:
                if "emailAddresses" in str(e):
                    pass
                else:
                    logging.warning(
                        "[Contact.py] Exception Error at {}, returning KeyError {}".format(
                            datetime.now(), str(e)
                        )
                    )

        return data

    @staticmethod
    def _get_domain(data):
        """Get the domain.

        The domain are the right side after @, in other words:
        email => "teste@abcde.com" means
        domain => "@abcde.com"

        Parameters
        ----------
        data : Union[Dict, Contact]
            Contact specific data, given in a dict format ou Contact object

        Returns
        -------
        str
            String containing the domain

        """
        return data["email"].split("@")[1]

    @staticmethod
    def get_unique_domains(data):
        """Get a set of unique domains in a list of contacts.

        Parameters
        ----------
        data : List
            A list with multiples contacts

        Returns
        -------
        set
            A set composed by unique domains found in data

        """
        domains = set()

        for connection in data:
            domains.add(Contact._get_domain(connection))

        return domains

    @staticmethod
    def group_by_email_group(data):
        """Get a grouped by domains list of contacts.

        This methods creates an dictionary with key as unique domain and pass
        a list of contacts with the same domain.

        Parameters
        ----------
        data : List
            List of contacts

        Returns
        -------
        dict
            Dictionary following this structure:
            {
                'domain1': [contact1, contact2],
                'domain2': [contact3, contact3]
            }

        """
        data = data["contacts"]

        domains = Contact.get_unique_domains(data)

        domains_grouped = {}

        for domain in domains:
            domains_grouped[domain] = []

        for connection in data:
            domains_grouped[Contact._get_domain(connection)].append(connection)

        return {"contacts": domains_grouped}
        
        
    @staticmethod
    def _get_specific_contact_informations(data):
        
        address = data.get("addresses", [{'streetAddress': 'Missing'}])[0].get("streetAddress")
        birth_date = data.get("birthdays", [{'text': 'Missing'}])[0].get("text")
        organization = data.get("organizations", [{'name': 'Missing'}])[0].get("name")
        occupation = data.get("organizations", [{'title': 'Missing'}])[0].get("title")
        
        return {
            'address': address,
            'birth_date': birth_date,
            'organization': organization,
            'occupation': occupation
        }
