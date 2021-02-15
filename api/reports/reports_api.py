"""Module for reports api."""
import requests
import json
from flask import request
from api.server import api_blueprint
from flask_restplus import Resource, reqparse, fields
from api.models.Contact import Contact

from api.ApiCodes import NO_AUTH_CODE, INVALID_CREDENTIALS

report_namespace = api_blueprint.namespace(
    "report", description="Generate reports"
)

@report_namespace.header(
    "authorization-code",
    "OAuth2 Access Token given by google api.",
    required=True,
)
@report_namespace.doc(
    responses={
        200: "OK",
        461: "Invalid Token",
        460: "No authorization-code in headers",
        462: "Another errors",
    },
)
@report_namespace.route("/")
class ReportApi(Resource):
    
    def get():
        ...