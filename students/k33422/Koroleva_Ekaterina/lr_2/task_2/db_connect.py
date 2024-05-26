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
    conn = get_connection()
    cur = conn.cursor()
    query = '''
    INSERT INTO "profiles"
        (user_id, first_name, last_name, middle_name, birth_date, gender, bio, country, city, language)
    VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''

    cur.execute(query, data)
    conn.commit()
    cur.close()
    conn.close()
