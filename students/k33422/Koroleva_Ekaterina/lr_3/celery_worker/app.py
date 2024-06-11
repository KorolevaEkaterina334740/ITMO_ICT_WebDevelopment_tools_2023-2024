import requests
from celery import Celery

from .utils import extract_data, insert_data

app = Celery(
    'celery_app',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0',
)


@app.task
def parse(url):
    doc = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
    data = extract_data(doc)
    for i in data:
        insert_data(i)

    return data
