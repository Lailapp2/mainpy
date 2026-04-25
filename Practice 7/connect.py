import psycopg2
from config import params

def connect():
    return psycopg2.connect(
        host=params["host"],
        database=params["database"],
        user=params["user"],
        password=params["password"]
    )