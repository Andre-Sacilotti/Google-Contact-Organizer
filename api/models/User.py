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
    query_id = TextField()
    name = TextField()
    contacts_statistics = MapField()
    
    
    @staticmethod
    def statistics_to_chart(data):
        """Return a dictionary with label and data to plot statistics.
        
        Parameters
        ----------
        data : Dict
            Dictionary with contacts statistics in the following format:
            {
                'organization': {
                    'google': 25, 'facebook': 30
                },
                ...
            }
            
        Returns
        -------
        dict
            Dictionary in the following format:
            {
                'organization': {
                    'label': ["google", "facebook", ...],
                    'data': [25, 30, ...]
                }
            }
        """
        data = data['contacts_statistics']
        
        chart_data = {}

        for key, item in data.items():
            print(key, item)
            chart_data[key] = {"label": [], "data": []}

            for label, value in item.items():
                chart_data[key]["label"].append(label)
                chart_data[key]["data"].append(value)

        return chart_data
