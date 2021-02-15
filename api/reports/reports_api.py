"""Module for reports api."""
import requests
import json
from flask import request
from api.server import api_blueprint
from flask_restplus import Resource, reqparse, fields
from api.contacts.contacts_api import ContactApi


import os

from firebase_admin import credentials, initialize_app, storage


import xlwt 
from xlwt import Workbook 

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
    
    def get(self):
        
        api = ContactApi()
        
        contacts = api._get_list_of_contacts(grouped=False)
        
        if contacts[1] == 200:
        
            wb = Workbook()
            sheet1 = wb.add_sheet('Contatos')
            
            line = 0
            column = 0
            for contact in ['Name', 'Email', 'JobTitle', 'Organization', "Region", "City"]:
                sheet1.write(line, column, contact)
                column += 1
            
            for contact in contacts[0]['contacts']:
                line += 1
                column = 0
                
                for key, value in contact.items():
                    if(str(key) == "id" or str(key) == 'photo_url'):
                        ...
                    else:
                        sheet1.write(line, column, value)
                        column += 1
                        
            wb.save('/tmp/test.xls')
            
            
            
            bucket = storage.bucket()
            blob = bucket.blob("/tmp/test.xls")
            blob.upload_from_filename("/tmp/test.xls")

            blob.make_public()
            
            return {'url': blob.public_url}, 200

        return contacts, 200