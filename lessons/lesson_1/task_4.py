# 4. Определение доступности веб-серверов:
#    *Синхронная реализация:*
#    В синхронной версии вы проверяете доступность каждого веб-сервера последовательно,
#    ожидая ответа от одного сервера перед переходом к следующему.
#    *Асинхронная реализация:*
#    В асинхронной версии вы можете отправить запросы к нескольким веб-серверам параллельно и ожидать ответов асинхронно.
#    Это позволяет быстрее определить доступность серверов.
import requests
import asyncio
import aiohttp
from utils.decorators import timeit

urls = [
        'https://ya.ru', 'https://www.rambler.ru', 'https://www.google.com', 'https://www.amazon.com',
        'https://lipetsk.mts.ru/personal', 'https://moskva.beeline.ru/customers/products/',
        'https://lc.megafon.ru', 'https://msk.tele2.ru',
        'https://www.x5.ru/ru/', 'https://magnit.ru'
        ]


# Синхронное определение доступности серверов
def sync_scrab(url):
    res = requests.get(url=url)
    if res.status_code == 200:
        return True
    else:
        return False


# Асинхронное определение доступности серверов
async def async_scrab(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, ssl=False) as content:
            if content.status == 200:
                return True
            else:
                return False


@timeit
def main1(urls):
    oks = []
    for index, url in enumerate(urls):
        if sync_scrab(url):
            oks.append(True)
        else:
            oks.append(False)
    return oks





@timeit
async def main2(urls):
    tasks = []
    for index, url in enumerate(urls):
        task = asyncio.create_task(async_scrab(url))
        tasks.append(task)
    return await asyncio.gather(*tasks)


if __name__ == '__main__':
    print(main1(urls))               # Время выполнения синхронной функции main1: 2.881664 сек.
    print(asyncio.run(main2(urls)))  # Время выполнения асинхронной функции main2: 0.775599 сек.
