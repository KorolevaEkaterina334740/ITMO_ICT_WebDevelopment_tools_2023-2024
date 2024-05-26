import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost",
        port="5432",
        database="travel",
        user="postgres",
        password="postgres",
    )

def insert_data(data):
    ...

