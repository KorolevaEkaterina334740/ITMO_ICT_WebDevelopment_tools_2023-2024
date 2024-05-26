import multiprocessing
import time

import requests

from task_2.db_connect import insert_data
from task_2.parsing import extract_data


def get(url: str) -> str:
    return requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text


def parse_and_save(url):
    html = get(url)
    data = extract_data(html)

    for item in data:
        insert_data(item)


def main(pages):
    base_url = 'https://traveling.by/fellows'

    tasks = []
    for page in range(1, pages + 1):
        url = f'{base_url}?page={page}'
        tasks.append(
            multiprocessing.Process(
                target=parse_and_save,
                args=(url,),
            )
        )

    start_time = time.perf_counter()
    for task in tasks:
        task.start()
    for task in tasks:
        task.join()
    end_time = time.perf_counter()

    print(f'Время выполнения: {end_time - start_time:.3f} секунд')


if __name__ == '__main__':
    main(10)
