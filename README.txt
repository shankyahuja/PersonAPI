/******************************************Application Description********************************************/

This application is a personal Information register API which provides features to read, add, update and delete operations through the PersonAPI.

The code structure is divided into various modules:

1. With a separate database.py and models.py file, we establish our sqlalchemy database table classes and connection a single time, then call them later as needed.

2. To avoid confusion between the SQLAlchemy models and the Pydantic models, we will have the file models.py with the SQLAlchemy models, and the file schemas.py with the Pydantic models

3. crud.py - To perform crud operations on sqlalchemy database using models.

4. main.py - here we bring all modular components together and also define our api endpoints. 



/*******************************Deployment Steps************************************************************/

1. Run the Dockerfile to build the image from PersonAPI project directory using below command:

	docker build -t personapiimage .

2. verify that the personapiimage is created using below command:

	docker images

3. Run the application using below command:

	docker run -d --name personapicontainer -p 10000:10000 personapiimage

4. Verify the Interactive API docs :  http://127.0.0.1:10000/docs

5. Verify the alternative API docs: http://127.0.0.1:10000/redoc

6. Authorize the application by providing an API Key (auth_token) on http://127.0.0.1:10000/docs : 1234567asdfgh

7. Run one time full data load on sqlalchemy database by calling the put method: http://127.0.0.1:10000/load_data

8. Run the GET method to read a person's details based on the ID: example http://127.0.0.1:10000/person/1

9. Run the POST method to add/update a person by providing person details in Request Body: http://127.0.0.1:10000/person/ 

10. Run the DELETE method to delete a person based on ID: http://127.0.0.1:10000/person/2


/*******************************Unit tests*********************************************************************/


Run the unit test cases from PersonAPI folder:

pip install pytest
pytest
