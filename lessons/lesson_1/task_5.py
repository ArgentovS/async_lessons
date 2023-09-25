# 5. Обработка большой очереди задач:
#    *Синхронная реализация:*
#    В синхронной версии вы обрабатываете задачи в очереди последовательно, что может вызвать задержки,
#    если одна из задач выполняется долго.
#    *Асинхронная реализация:*
#    В асинхронной версии вы можете обрабатывать задачи в очереди параллельно,
#    что уменьшает общее время обработки задач и улучшает отзывчивость системы.

import time
import asyncio
import random
from utils.decorators import timeit

time_periods = [elem for elem in range(1, 6)]
print(time_periods)


# Синхронные задачи выполнение очереди задач
def sync_sleep(period):
    time.sleep(period)
    print(f'Прошло: {period} сек.')


# Асинхронные задачи выполнение очереди задач
async def async_sleep(period):
    await asyncio.sleep(period)
    print(f'Прошло: {period} сек.')


# Синхронное выполнение задач
@timeit
def main1(periods):
    for period in time_periods:
        sync_sleep(period)


# Асинхронное выполнение задач
@timeit
async def main2(periods):
    tasks = []
    for period in periods:
        task = asyncio.create_task(async_sleep(period))
        tasks.append(task)
    return await asyncio.gather(*tasks)


if __name__ == '__main__':
    main1(time_periods)               # Время выполнения синхронной функции main1: 15.019326 сек.
    asyncio.run(main2(time_periods))  # Время выполнения асинхронной функции main2: 5.002013 сек.
