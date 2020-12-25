# Setting up the environment
1. Create a the virtual environment and install all the requirements or dependencies.
```code
>>> python3 -m venv venv
>>> source venv/Scripts/activate
>>> pip install -r requirements.txt
```
2. Create a mySQL database with the following credentials. Also, run the following scripts to initialize the database.
```code
DATABASE CREDENTIALS

USER     =  root
PASSWORD =  password
```
```code
*RUN THIS SCRIPT*
-----------------
CREATE DATABASE Assessment;


INSERT INTO 
    _admin
VALUES 
    ('admin', 'password');


INSERT INTO 
    _Options
VALUES 
    (1, 'Strongly Agree', 2), 
    (2, 'Agree', 1), 
    (3, 'Neutral', 0), 
    (4, 'Disagree', -1), 
    (5, 'Strongly Disagree', -2);
```
3. Import the `Assessment.postman_collection.json` file in the POSTMAN app/web.
4. Run the `Flask App`.
```code
>>> python main.py
```

# Testing using POSTMAN
> Accepted `JSON` formats for the API.
```code
1) Register User

    {
        "details": {
            "firstname": "Amit",
            "lastname": "Pathak",
            "email": "amit.pathak@email.com",
            "username": "amit_pathak",
            "password": "qwerty123"
        }
    }

2) Login User

    {
        "username": "amit_pathak",
        "password": "qwerty123"
    }

3) Delete User

    {
        "username": "amit_pathak",
        "password": "qwerty123"
    }

4) Submit Response

    {
        "response": {
            "1": 2, "2": 3, "3":1, "4":5, "5":1, "6":1, "7":2
        }
    }

    > 1 - 'Strongly Agree'
    > 2 - 'Agree'
    > 3 - 'Neutral'
    > 4 - 'Disagree'
    > 5 - 'Strongly Disagree'

5) Admin Login

    {
        "admin": {
            "username": "admin",
            "password": "password"
        }
    }

6) Update Questions

    {
        "update_questions": {
            "10": "This is an updated 10th question",
            "9": "Updating 9th question"
        }
    }

7) Delete Question

    {
        "delete_questions": [2, 3, 10]
    }
```
