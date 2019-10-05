from flask import Flask
from flask_restful import Api, Resource
from endpoints.registrations import Registrations
from endpoints.candidates import Candidates
from endpoints.candidate import Candidate

app = Flask(__name__)
app.config['BUNDLE ERRORS'] = True
api = Api(app, catch_all_404s=True)

api.add_resource(Registrations, '/hrms/v1/registrations', methods=['POST'])
api.add_resource(Candidates,'/hrms/v1/candidates', methods=['GET'])
api.add_resource(Candidate,'/hrms/v1/candidates/<string:id>', methods=['GET'])

if __name__ == '__main__':
    app.run(host='0.0.0.0')
