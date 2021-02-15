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
    organization : str
        Contact organization that works/study/volunteer
    job : str
        Contact job title, like developer, manager
    city : str
        Contact city.
    region : str.
        Contact city

    """

    id = TextField(primary_key=True)
    name = TextField()
    photo_url = TextField()
    email = TextField()
    organization = TextField()
    job = TextField()
    city = TextField()
    region = TextField()

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
            "job": self.job,
            "organization": self.organization,
            "region": self.region,
            "city": self.city,
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
            "job":
            "organization":
            "region":
            "city":
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
            job=data["job"],
            organization=data["organization"],
            region=data["region"],
            city=data["city"],
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
                    organization=connection.get(
                        "organizations", [{"name": "Missing"}]
                    )[0]["name"],
                    job=connection.get(
                        "organizations", [{"title": "Missing"}]
                    )[0]["title"],
                    city=connection.get("addresses", [{"city": "Missing"}])[0][
                        "city"
                    ],
                    region=connection.get(
                        "addresses", [{"region": "Missing"}]
                    )[0]["region"],
                )
                data["contacts"].append(new_contact.to_dict())
                print(new_contact.to_dict())
                print("\n\n")
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
    def _get_organization(data):
        """Get the organization.

        Parameters
        ----------
        data : Union[Dict, Contact]
            Contact specific data, given in a dict format ou Contact object

        Returns
        -------
        str
            String containing the organization

        """
        return data.get("organization", "Missing")

    @staticmethod
    def _get_job(data):
        """Get the job title.

        Parameters
        ----------
        data : Union[Dict, Contact]
            Contact specific data, given in a dict format ou Contact object

        Returns
        -------
        str
            String containing the job title

        """
        return data.get("job", "Missing")

    @staticmethod
    def _get_city(data):
        """Get the city.

        Parameters
        ----------
        data : Union[Dict, Contact]
            Contact specific data, given in a dict format ou Contact object

        Returns
        -------
        str
            String containing the city

        """
        return data.get("city", "Missing")

    @staticmethod
    def _get_region(data):
        """Get the organization.

        Parameters
        ----------
        data : Union[Dict, Contact]
            Contact specific data, given in a dict format ou Contact object

        Returns
        -------
        str
            String containing the organization

        """
        return data.get("region", "Missing")

    @staticmethod
    def get_unique_organizations(data):
        """Get a set of unique organizations in a list of contacts.

        Parameters
        ----------
        data : List
            A list with multiples contacts

        Returns
        -------
        set
            A set composed by unique organizations found in data

        """
        domains = set()

        for connection in data:
            domains.add(Contact._get_organization(connection))

        return domains

    @staticmethod
    def get_unique_job(data):
        """Get a set of unique job in a list of contacts.

        Parameters
        ----------
        data : List
            A list with multiples contacts

        Returns
        -------
        set
            A set composed by unique job found in data

        """
        domains = set()

        for connection in data:
            domains.add(Contact._get_job(connection))

        return domains

    @staticmethod
    def get_unique_city(data):
        """Get a set of unique city in a list of contacts.

        Parameters
        ----------
        data : List
            A list with multiples contacts

        Returns
        -------
        set
            A set composed by unique city found in data

        """
        domains = set()

        for connection in data:
            domains.add(Contact._get_city(connection))

        return domains

    @staticmethod
    def get_unique_region(data):
        """Get a set of unique region in a list of contacts.

        Parameters
        ----------
        data : List
            A list with multiples contacts

        Returns
        -------
        set
            A set composed by unique region found in data

        """
        domains = set()

        for connection in data:
            domains.add(Contact._get_region(connection))

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
    def get_quantity_per_domain(data):
        """Get a dict with quantity of contacts per domain

        This methods creates an dictionary with key as unique domain and pass
        a integer number representing how much contacts has this domain

        Parameters
        ----------
        data : List
            List of contacts

        Returns
        -------
        dict
            Dictionary following this structure:
            {
                'domain1': 3,
                'domain2': 1
            }

        """
        data = data["contacts"]

        domains = Contact.get_unique_domains(data)

        domains_grouped = {}

        for domain in domains:
            domains_grouped[domain] = 0

        for connection in data:
            domains_grouped[Contact._get_domain(connection)] += 1

        return {"contacts": domains_grouped}

    @staticmethod
    def _get_specific_contact_informations(data):
        """Return specific information about a contact.
        
        Parameters
        ----------
        data : dict
            Dictionary returned from google people api request
            
        Returns
        -------
        dict
            Dictionary with only desired informations.
            {
                "address": address,
                "birth_date": birth_date,
                "organization": organization,
                "occupation": occupation,
            }

        """
        address = data.get("addresses", [{"streetAddress": "Missing"}])[0].get(
            "streetAddress"
        )
        birth_date = data.get("birthdays", [{"text": "Missing"}])[0].get(
            "text"
        )
        organization = data.get("organizations", [{"name": "Missing"}])[0].get(
            "name"
        )
        occupation = data.get("organizations", [{"title": "Missing"}])[0].get(
            "title"
        )

        return {
            "address": address,
            "birth_date": birth_date,
            "organization": organization,
            "occupation": occupation,
        }

    @staticmethod
    def get_quantity_per_organization(data):
        """Get a dict with quantity of contacts per organization

        Parameters
        ----------
        data : List
            List of contacts

        Returns
        -------
        dict
            Dictionary following this structure:
            {
                'organization1': 3,
                'organization2': 1
            }

        """
        data = data["contacts"]

        organizations = Contact.get_unique_organizations(data)

        organizations_grouped = {}

        for org in organizations:
            organizations_grouped[org] = 0

        for connection in data:
            organizations_grouped[Contact._get_organization(connection)] += 1

        return {"contacts": organizations_grouped}

    @staticmethod
    def get_quantity_per_job(data):
        """Get a dict with quantity of contacts per job

        Parameters
        ----------
        data : List
            List of contacts

        Returns
        -------
        dict
            Dictionary following this structure:
            {
                'job_title1': 3,
                'job_title2': 1
            }

        """
        data = data["contacts"]

        jobs = Contact.get_unique_job(data)

        jobs_grouped = {}

        for job in jobs:
            jobs_grouped[job] = 0

        for connection in data:
            jobs_grouped[Contact._get_job(connection)] += 1

        return {"contacts": jobs_grouped}

    @staticmethod
    def get_quantity_per_city(data):
        """Get a dict with quantity of contacts per city

        Parameters
        ----------
        data : List
            List of contacts

        Returns
        -------
        dict
            Dictionary following this structure:
            {
                'city1': 3,
                'city2': 1
            }

        """
        data = data["contacts"]

        citys = Contact.get_unique_city(data)

        city_grouped = {}

        for city in citys:
            city_grouped[city] = 0

        for connection in data:
            city_grouped[Contact._get_city(connection)] += 1

        return {"contacts": city_grouped}

    @staticmethod
    def get_quantity_per_region(data):
        """Get a dict with quantity of contacts per region

        Parameters
        ----------
        data : List
            List of contacts

        Returns
        -------
        dict
            Dictionary following this structure:
            {
                'region1': 3,
                'region2': 1
            }

        """
        data = data["contacts"]

        regions = Contact.get_unique_region(data)

        region_grouped = {}

        for region in regions:
            region_grouped[region] = 0

        for connection in data:
            region_grouped[Contact._get_region(connection)] += 1

        return {"contacts": region_grouped}


