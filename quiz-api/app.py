import datetime
from flask import Flask, request
import hashlib
from flask_cors import CORS
import hashlib
import jwt
import sqlite3
from models import Question
from db_helpers import insert_question

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200


secret = "Groupe Henri Victor"
expiration_in_seconds = 3600


def build_token():
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=expiration_in_seconds),
            'iat': datetime.datetime.utcnow(),
            'sub': 'quiz-app-admin'
        }
        return jwt.encode(
            payload,
            secret,
            algorithm="HS256"
        )
    except Exception as e:
        return e
    
@app.route('/login', methods=['POST'])
def getPassword():
    payload = request.get_json()
    tried_password = payload['password'].encode('utf-8')
    hashed = hashlib.md5(tried_password).digest()
    
    if hashed == b'\xd8\x17\x06PG\x92\x93\xc1.\x02\x01\xe5\xfd\xf4_@':
        access_token = {}
        access_token['token'] = build_token()
        return access_token
    return 'Unauthorized', 401

@app.route('/questions', methods=['POST'])
def insertQuestion():
    #Récupérer le token envoyé en paramètre
    request.headers.get('Authorization')

    #récupèrer un l'objet json envoyé dans le body de la requète
    # print(request.get_json())

    json = request.get_json()
    input_question = Question.from_json(json)

    question_id = insert_question(input_question)


    return {"id": question_id}

    #Retourner l'id de la question


if __name__ == "__main__":
    app.run()
