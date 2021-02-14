from api.server import api_blueprint
from flask_restplus import Resource, fields
from flask import request
from api.ApiCodes import NO_AUTH_CODE, INVALID_CREDENTIALS
from api.models.User import User
from api.contacts.contacts_api import ContactApi


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
            email = data.get("user_email", None)
            
            if id is None or name is None or email is None:
                return {"error": "Some body arguments is missing. It needs id, email and name"}, 463
            
            user = User(
                id=id,
                name=name,
                email=email
                            )
            
            user.save()
            
            auxapi = ContactApi()
            
            print("running API")
            print(auxapi._get_list_of_contacts())
            print("Finished API")
            
        else:
            return NO_AUTH_CODE
