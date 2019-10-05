from flask_restful import Resource, reqparse
from . import db

class Candidates(Resource):
## This class is for admin use only. It is used to retrieve all the details for all the candidates in the database table sorted by date in descending order.
    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('X-ADMIN', type=int, required=True, location='headers')
        args = parser.parse_args()
        if args['X-ADMIN'] is not 1:
            return {
                "message":{
                    "error":"Unauthorized."
                }
            },401
        all_candidates = []
        cursor = db.cursor()
        cursor.execute("SELECT candidate_id, full_name, dob, department, years_of_experience, regisrtation_date FROM candidate_details ORDER BY regisrtation_date DESC")
        list_of_candidates = cursor.fetchall()
        for item in list_of_candidates:
            candidate = {
                "candidate_id" : item[0],
                "full_name": item[1],
                "dob":str(item[2]),
                "department":item[3],
                "years_of_experience":item[4],
                "registration_date": str(item[5])
            }
            all_candidates.append(candidate)
        return {
            "metadata":{
                "offset":None,
                "limit": None,
                "count":len(all_candidates)
            },
            "data":all_candidates
        }
