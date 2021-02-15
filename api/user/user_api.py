from api.server import api_blueprint
from flask_restplus import Resource, fields
from flask import request
from api.ApiCodes import NO_AUTH_CODE, INVALID_CREDENTIALS
from api.models.User import User
from api.contacts.contacts_api import ContactApi
from api.models.Contact import Contact
import json


user_namespace = api_blueprint.namespace(
    "user", description="Create and manage Users data"
)

model = user_namespace.model(
    "User",
    {
        "user_id": fields.String(
            description="User unique identifier given by google"
        ),
        "user_email": fields.String(description="User principal email"),
        "user_name": fields.String(description="User complete name"),
    },
)


@user_namespace.doc(
    responses={
        200: "OK",
        461: "Invalid Token",
        460: "No authorization-code in headers",
        462: "Another errors",
        463: "Argument missing in request data",
        465: "User Not Found",
    }
)
@user_namespace.route("/")
class UserApi(Resource):
    @user_namespace.header(
        "authorization-code",
        "OAuth2 Access Token given by google api.",
        required=True,
    )
    @user_namespace.doc(body=model)
    def put(self):

        token = request.headers.get("authorization-code")
        if token is not None:
            data = request.get_json(force=True)

            id = data.get("user_id", None)
            name = data.get("user_name", None)

            if id is None or name is None:
                return (
                    {
                        "error": "Some body arguments is missing. It needs id, email and name"
                    },
                    463,
                )

            user = User(id=id, name=name, query_id=id)

            auxapi = ContactApi()

            contacts = auxapi._get_list_of_contacts(grouped=False)

            if contacts[1] == 200:
                contacts_statistics = Contact.get_quantity_per_domain(
                    contacts[0]
                )
                contacts_statistics_organization = Contact.get_quantity_per_organization(
                    contacts[0]
                )
                contacts_statistics_jobtitle = Contact.get_quantity_per_job(
                    contacts[0]
                )
                contacts_statistics_city = Contact.get_quantity_per_city(
                    contacts[0]
                )
                contacts_statistics_region = Contact.get_quantity_per_region(
                    contacts[0]
                )

                user.contacts_statistics = {
                    "domain": contacts_statistics["contacts"],
                    "organization": contacts_statistics_organization[
                        "contacts"
                    ],
                    "jobtitle": contacts_statistics_jobtitle["contacts"],
                    "city": contacts_statistics_city["contacts"],
                    "region": contacts_statistics_region["contacts"],
                }
                user.save()
                return {"success": "User Saved"}, 200

            return contacts

        else:
            return NO_AUTH_CODE

    @user_namespace.doc(
        params={
            "userId": "User unique id to get data on Firebase DB",
            "toChart": """Specify this =true if you wanna to retrive statistics \
        in a format like:
            'organization':
             {
                'label': ["Google", "Facebook", "Conecta Nuvem"],
                'data': [25, 10, 259]
            }
        """,
        }
    )
    def get(self):
        print(request)
        data = request.args
        user_data = User.collection.filter(query_id=data.get("userId", None))

        if data.get("toChart", None) == "true":
            if user_data.get() is not None:
                
                return User.statistics_to_chart(
                    user_data.get().to_dict()
                ), 200
                
            else:
                return {"error": "User not found."}, 465
        else:
            if user_data.get() is not None:
                return user_data.get().to_dict(), 200
            else:
                return {"error": "User not found."}, 465
