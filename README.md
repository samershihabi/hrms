
# HRMS REST API Endpoints

This repository contains the python3 code for a simple HRMS system. It contains 3 API endpoints, and is written in Flask-RESTful and MariaDB backend.

The python3 code is structured into classes, each class represents an API endpoint. app.py gives a high level view on how the endpoints are designed.

Users of this API can upload their resumes and details via the POST request. Admins can download the list of candidates as well as fetch a specific candidate by Id and download their resume locally.

This repository also contains the YAML File for the Swagger (OpenAPI) interactive documentation for the APIs
here's a link to see the interactive documentation
link: https://app.swaggerhub.com/apis/samershihabi/HRMS/1.0.0

# How to run the CODE

1 - clone this repo and change directory to hrms.

2 - Install MariaDB locally. 

3 - create a database called candidates(Username: root , Password: liwwa123) that contains a table called candidate_details 

4 - type pip install -r requirements.txt in the command line to install the required dependencies.

5 - type python app.py to start the server!

note: The swagger doc contains all the required documentation once the application is hosted, anyone can call the APIs directly through the interactive swagger doc.
If you don't wish to use the swagger doc, app.py contains all the endpoints and the code itself is pretty self-explanatory.

# Things to Improve

Increase security of the APIs

Hosting the APIs and the database on a virtual private server for public access.

Proper error Handling and Rollback on inserts and database transactions.

Thanks!
