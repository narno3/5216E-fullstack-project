from models import Question
import sqlite3
from flask import flash

def insert_question(input_question: Question) -> int:
    """inserts question into sqlite database"""
    question_id = -1

    db_connection = sqlite3.connect("./database.db")

    # set the sqlite connection in "manual transaction mode"
    # (by default, all execute calls are performed in their own transactions, not what we want)
    db_connection.isolation_level = None

    #Create cursor
    cur = db_connection.cursor()

    # start transaction
    cur.execute("begin")
    try :
        cur.execute(
            f"INSERT INTO Questions (position, title, text, image) VALUES"
            f'({input_question.position}, "{input_question.title}", "{input_question.text}", "{input_question.image}")'
        )

        # send the request
        cur.execute("commit") 

        query = cur.execute(f"SELECT id from Questions WHERE position = {input_question.position}")
        question_id = query.fetchone()[0]


    # in case of exception, rollback the transaction
    except Exception as e:
        cur.execute('rollback')
        cur.close()
        flash(e)

    cur.close()
    return question_id