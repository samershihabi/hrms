from flask_restful import Resource, reqparse
from . import db
import base64

class Candidate(Resource):
## This class is used to retrieve resume for a single candidate by Id from MariaDB, decode the file, and download it.
## The class is referenced in app.py resources. Only admin users are allowed to use this feature.

    def get(self,id):
        parser = reqparse.RequestParser()
        parser.add_argument('X-ADMIN', type=int, required=True, location='headers')
        args = parser.parse_args()
        if args['X-ADMIN'] is not 1:
            return {
                "message":{
                    "error":"Unauthorized."
                }
            },401
        cursor = db.cursor()
        cursor.execute("SELECT full_name, resume, document_format FROM candidate_details WHERE candidate_id=%s",(id,))
        document = cursor.fetchone()

        with open(document[0]+'.'+document[2] , 'wb') as resume_file:
            resume_file.write(base64.b64decode(document[1]))

        # the below line of code is for saving the resume in an S3 bucket
        # boto3.client(‘s3’).upload_file(document[0]+'.'+document[2], <bucket_name>, document[0]+'.'+document[2])
        return {
            "metadata":{
                "size":None,
                "format": None,
            },
            "data": {
                "message":"File Downloaded Successfully",
                "candidate_name": document[0],
                "base64": document[1]
            },
        }, 200
