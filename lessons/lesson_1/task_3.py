# 3. Чтение данных из нескольких файлов:
#   *Синхронная реализация:*
#   В синхронной версии вы читаете данные из каждого файла последовательно,
#   ожидая завершения чтения одного файла перед началом чтения следующего.
#   *Асинхронная реализация:*
#   В асинхронной версии вы можете читать данные из нескольких файлов параллельно,
#   что может ускорить обработку данных, если файлы независимы друг от друга.


import random
import asyncio
import aiofiles
from utils.decorators import timeit
from typing import List

PATH_FILE = '../../data/lesson_1_task_3/file'

def func_generator_file(elem):
    file_name = f'{PATH_FILE}_{elem+1}.txt'
    string: str = ''
    for i in range(random.randint(1000000, 2000000)):
        string += str(i)
        if i % 100 == 0:
            string += '\n'

    with open(file_name, 'w') as file:
        file.write(string)
    return file_name


# Сгенерируем длинные текстовые файлы
files_name: List = [func_generator_file(elem) for elem in range(10)]


# Синхронное чтение файлов
@timeit
def sync_read(files_name):
    results = []
    for name in files_name:
        with open(name, 'r') as file:
            resulat = file.read()
        results.append(resulat)
    return results


# Асинхронное чтение файлов
async def async_read(name):
    async with aiofiles.open(name, 'r') as file:
        result = await file.read()
    return result


@timeit
async def main2(files_name):
    tasks = []
    for name in files_name:
        task = asyncio.create_task(async_read(name))
        tasks.append(task)
    return await asyncio.gather(*tasks)


if __name__ == '__main__':
    sync_read(files_name)               # Время выполнения синхронной функции sync_read: 0.022720 сек.
    asyncio.run(main2(files_name))      # Время выполнения асинхронной функции main2: 0.017425 сек.
