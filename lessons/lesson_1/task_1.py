# 1. Загрузка изображений по URL:
#    *Синхронная реализация:*
#    В синхронном подходе вы последовательно загружаете изображения по URL и сохраняете их на диск.
#    Это означает, что каждое изображение будет загружено после завершения предыдущего.
#    *Асинхронная реализация:*
#    В асинхронном подходе вы используете множество параллельных запросов для загрузки изображений,
#    что может существенно сократить время загрузки, особенно если есть много изображений.

import requests
import asyncio
import aiohttp
from utils.decorators import timeit

urls = [
        'https://w.forfun.com/fetch/76/76aa0386ecd0681229a784b9b27776ed.jpeg?h=1200&r=0.5',
        'https://w.forfun.com/fetch/4e/4e77462fd7f95995ccb8ff5147acc573.jpeg?h=1200&r=0.5',
        'https://w.forfun.com/fetch/82/82f78332d20e46024b868a1ec001f833.jpeg?h=1200&r=0.5',
        'https://w.forfun.com/fetch/8d/8d1b2fdd387d376d997596abd93c6268.jpeg?h=1200&r=0.5',
        'https://w.forfun.com/fetch/57/5705b274c16e6d7478479dcfc32e0bfe.jpeg?h=1200&r=0.5',
        'https://w.forfun.com/fetch/60/607d27f3d5e15b07958f603d5a9215a6.jpeg?h=1200&r=0.5',
        'https://w.forfun.com/fetch/48/48c003334783769fef7bf6c02ecfea81.jpeg?h=1200&r=0.5',
        'https://w.forfun.com/fetch/4e/4e79ee29da2685947848e7a03e824411.jpeg?h=1200&r=0.5',
        'https://w.forfun.com/fetch/01/01c91cfdb4cac3029bd3b07b8ce9d94f.jpeg?h=1200&r=0.5',
        'https://w.forfun.com/fetch/c0/c0a1ac30cfed77becf946f9238a353fd.jpeg?h=1200&r=0.5'
        ]
PATH_PHOTO = '../../data/lesson_1/photo'


# Синхронное скачивание
def sync_scrab(index, url):
    res = requests.get(url=url)
    with open(f'{PATH_PHOTO}_{index+1}.jpeg', 'wb') as file:
        file.write(res.content)


# Асинхронное скачивание
async def async_scrab(index, url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, ssl=False) as content:
            res = await content.read()
            with open(f'{PATH_PHOTO}_{index+1}.jpeg', 'wb') as file:
                file.write(res)


@timeit
def main1(urls):
    for index, url in enumerate(urls):
        sync_scrab(index, url)


@timeit
async def main2(urls):
    tasks = []
    for index, url in enumerate(urls):
        task = asyncio.create_task(async_scrab(index, url))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    main1(urls)               # Время выполнения функции main1: 4.884244 сек.
    asyncio.run(main2(urls))  # Время выполнения функции main2: 4.818635 сек.
