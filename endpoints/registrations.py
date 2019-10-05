from flask_restful import Resource, reqparse
import werkzeug
from . import db
import re
import datetime
import base64

class Registrations(Resource):
## This class is used to Submit a new application, including the candidate details as well as their resume.
## This endpoint has no access control; anybody can use it.
## Acceptable file formats are .PDF, and .DOCX.
## Acceptable departments are IT, HR, and Finance.
## Date should be in YYYY-MM-DD Format.

    def post(self):
        try:
            ALLOWED_EXTENSIONS = set(['PDF', 'DOCX'])
            parser = reqparse.RequestParser()
            parser.add_argument('resume', type=werkzeug.datastructures.FileStorage, required=True, location='files')
            parser.add_argument('full_name', type=str, required=True)
            parser.add_argument('dob', type=str, required=True)
            parser.add_argument('years_of_experience', type=int, required=True)
            parser.add_argument('department', type=str, required=True)
            args = parser.parse_args()
            # print(type(args.years_of_experience))
            encoded_resume = base64.b64encode(args['resume'].read());
            if not re.search(r'([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[0-1]))$',args.dob):
                return {
                    "message":{
                        "error": "Invalid Date Format."
                    }
                },400
            if args['department'].upper() not in ['HR','IT','FINANCE']:
                return {
                    "message":{
                        "error": "Allowed Departments Are HR, FINANCE, and IT"
                    }
                },400
            file_format = args['resume'].filename.rsplit('.',1)[1].upper()
            if file_format not in ALLOWED_EXTENSIONS:
                return {
                    "message":{
                        "error": "File Extension Is Not Supported."
                    }
                },400
            dob = datetime.datetime.strptime(args['dob'], '%Y-%m-%d')
            registration_date = datetime.date.today()
            cursor = db.cursor()
            cursor.execute("INSERT INTO candidate_details (full_name,dob,department,years_of_experience,resume,regisrtation_date,document_format) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                            (args['full_name'],
                            args['dob'],
                            args['department'],
                            args['years_of_experience'],
                            encoded_resume,
                            registration_date,
                            file_format))
            db.commit()

            return {
                "message":{
                    "success": "Record Created."
                }
            },201
        except Exception as e:
            print(e)
