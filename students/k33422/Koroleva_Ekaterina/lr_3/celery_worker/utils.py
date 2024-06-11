from datetime import date

import psycopg2
from bs4 import BeautifulSoup


def extract_data(html):
    results = []

    soup = BeautifulSoup(html, 'html.parser')

    for section in soup.select('#fellow_block section'):
        first_name_age = section.select_one('.user_name strong').get_text(strip=True).split(', ')
        first_name = first_name_age[0]
        age = first_name_age[1] if len(first_name_age) > 1 else 0
        country_city = section.select_one('.user_name span').get_text(strip=True).split(', ')
        country = country_city[0]
        city = country_city[1] if len(country_city) > 1 else 'Unknown'
        bio = section.select_one('dt:contains("О себе:") + dd').get_text(strip=True)

        birth_date = date(date.today().year - int(age), 1, 1).strftime('%Y-%m-%d')

        results.append(
            (1, first_name, 'Unknown', 'Unknown', birth_date, 'MALE', bio, country, city, 'Russian')
        )

    return results


def get_connection():
    return psycopg2.connect(
        host="database",
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
