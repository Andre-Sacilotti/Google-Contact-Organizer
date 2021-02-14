from api.server import api_blueprint
from flask_restplus import Resource, fields
from flask import request
from api.ApiCodes import NO_AUTH_CODE, INVALID_CREDENTIALS
from api.models.User import User
from api.contacts.contacts_api import ContactApi
from api.models.Contact import Contact


user_namespace = api_blueprint.namespace(
    "user", description="Create and manage Users data"
)

model = user_namespace.model('User', {
    'user_id': fields.String(description="User unique identifier given by google"),
    'user_email': fields.String(description="User principal email"),
    'user_name': fields.String(description="User complete name")
})

@user_namespace.doc(
    responses={
        200: "OK",
        461: "Invalid Token",
        460: "No authorization-code in headers",
        462: "Another errors",
        463: "Argument missing in request data"
    }
)
@user_namespace.header(
    "authorization-code",
    "OAuth2 Access Token given by google api.",
    required=True,
)
@user_namespace.route("/")
@user_namespace.doc(body=model)
class UserApi(Resource):
    
    @user_namespace.doc(body=model)
    def put(self):
        
        token = request.headers.get("authorization-code")
        if token is not None:
            data = request.get_json(force=True)
            
            id = data.get("user_id", None)
            name = data.get("user_name", None)
            
            if id is None or name is None:
                return {"error": "Some body arguments is missing. It needs id, email and name"}, 463
            
            user = User(
                id=id,
                name=name)
            
            auxapi = ContactApi()
            
            contacts = auxapi._get_list_of_contacts(grouped=False)
            
            if contacts[1] == 200:
                contacts_statistics = Contact.get_quantity_per_domain(contacts[0])
                
                contacts_statistics_organization = Contact.get_quantity_per_organization(contacts[0])
                
                user.contacts_statistics = {
                    "domain": contacts_statistics['contacts'],
                    'organization': contacts_statistics_organization['contacts']
                    }
                user.save()
                return "a", 200
                
            return contacts
            
        else:
            return NO_AUTH_CODE
