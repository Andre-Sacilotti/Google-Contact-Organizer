"""Module for contact api."""
import requests
import json
from flask import request
from api.server import api_blueprint
from flask_restplus import Resource, reqparse, fields
from api.models.Contact import Contact

from api.ApiCodes import NO_AUTH_CODE, INVALID_CREDENTIALS

contact_namespace = api_blueprint.namespace(
    "contact", description="Read and manage Contacts"
)

parser = reqparse.RequestParser()
parser.add_argument('personId', type=str, location='args')

@contact_namespace.header(
    "authorization-code",
    "OAuth2 Access Token given by google api.",
    required=True,
)
@contact_namespace.doc(
    responses={
        200: "OK",
        461: "Invalid Token",
        460: "No authorization-code in headers",
        462: "Another errors",
    },
    params = {
        'personID': """If you pass the personId Query it will return an specific contact data. Otherwise it will return a list with all contatcs"""
    }
)
@contact_namespace.route("/")
class ContactApi(Resource):
    """Restful API to deal with contacts."""
    
    def _get_specific_contact(self, personId):
        token = request.headers.get("authorization-code")
        if token is not None:
            authorization_header = {"Authorization": "Bearer %s" % token}

            r = requests.get(
                "https://people.googleapis.com/v1/people/{contact_id}?personFields={query}".format(
                    contact_id=personId, query="birthdays,addresses,organizations"
                ),
                headers=authorization_header,
            )

            json_data = json.loads(r.text)
            
            if json_data.get("error", None) is not None:
                if json_data["error"]["code"] == 401:
                    return INVALID_CREDENTIALS
                else:
                    # Outros tipos de erros
                    return json_data, 462
            json_data = Contact._get_specific_contact_informations(json_data)
                
            return json_data, 200
        else:
            return NO_AUTH_CODE
    
    def _get_list_of_contacts(self, grouped=True):
        token = request.headers.get("authorization-code")
        if token is not None:
            authorization_header = {"Authorization": "Bearer %s" % token}

            r = requests.get(
                "https://people.googleapis.com/v1/people/me/connections?personFields=names,emailAddresses,photos,addresses,organizations",
                headers=authorization_header,
            )

            json_data = json.loads(r.text)

            if json_data.get("error", None) is not None:
                if json_data["error"]["code"] == 401:
                    return INVALID_CREDENTIALS
                else:
                    # Outros tipos de erros
                    return json_data, 462
            else:
                # Processar os dados e transformar em algo simples p/ front

                objects = Contact.multiples_json_contacts_to_objects(json_data)
                
                if(grouped):
                    grouped_by_domains = Contact.group_by_email_group(objects)
                    sorted(
                        grouped_by_domains,
                        key=lambda k: len(grouped_by_domains[k]),
                        reverse=False,
                    )
                    return (grouped_by_domains, 200)
                else:
                    print(objects)
                    return (objects, 200)

        else:
            return NO_AUTH_CODE

    def get(self):
        """Get methods that returns an contact specific information or a list with grouped contat"""
        
        args = parser.parse_args()
        
        if args['personId'] is None:
            return self._get_list_of_contacts()
        else:
            aux = self._get_specific_contact(args['personId'])
            return aux
            
            
