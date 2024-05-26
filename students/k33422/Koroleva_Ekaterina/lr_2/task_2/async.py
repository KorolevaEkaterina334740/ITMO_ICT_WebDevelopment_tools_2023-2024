import asyncio
import time

import aiohttp

from task_2.db_connect import insert_data
from task_2.parsing import extract_data


async def get(url: str) -> str:
    async with aiohttp.ClientSession(headers={'User-Agent': 'Mozilla/5.0'}) as session:
        async with session.get(url) as response:
            return await response.text()


async def parse_and_save(url):
    html = await get(url)
    data = extract_data(html)

    print(data)

    for item in data:
        insert_data(item)


async def main(pages):
    base_url = 'https://traveling.by/fellows'

    tasks = []
    for page in range(1, pages + 1):
        url = f'{base_url}?page={page}'
        tasks.append(asyncio.create_task(parse_and_save(url)))

    start_time = time.perf_counter()
    await asyncio.gather(*tasks)
    end_time = time.perf_counter()

    print(f'Время выполнения: {end_time - start_time:.3f} секунд')


if __name__ == '__main__':
    asyncio.run(main(10))
