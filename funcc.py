import psycopg2
from config import *


def rename(b=0):
    name = b
    b = str(b)
    b = b.replace("(", "")
    b = b.replace("'", "")
    b = b.replace(",", "")
    b = b.replace(")", "")
    return b

def db(id):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name)
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT user_name FROM bot_users WHERE user_name = '{id}';""")
            name = cursor.fetchone()
            print(name)
            name = rename(name)
    except Exception as _ex:
        print(_ex)
    finally:
        if connection:
            connection.close()
    return id
