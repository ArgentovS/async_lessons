# 2. Расчёт факториала для списка чисел:
#    *Синхронная реализация:*
#    В синхронной версии вы рассчитываете факториал каждого числа в списке последовательно,
#    что может занять много времени, если список большой.
#    *Асинхронная реализация:*
#    В асинхронной версии вы можете рассчитывать факториалы параллельно для всех чисел в списке,
#    что может ускорить выполнение, особенно при больших списках.

import random
import asyncio
from utils.decorators import timeit
from typing import List

# Сгенерируем длинный список целых чисел
numbers: List[int] = [random.randint(1, 270) for i in range(1, 60000)]


# Функия рекурентного расчёта факториала
def fact(number):
    if number == 1:
        return 1
    else:
        return number * fact(number - 1)



# Синхронный расчёт факториалов длинного списка
@timeit
def sync_calc(numbers):
    factorials = []
    for elem in numbers:
        factorial = fact(elem)
        factorials.append(factorial)
    return factorials


# Асинхронное расчёт факториалов длинного списка
async def async_fact(number):
    factorial = fact(number)
    return factorial


@timeit
async def main2(numbers):
    tasks = []
    for elem in numbers:
        task = asyncio.create_task(async_fact(elem))
        tasks.append(task)
    return await asyncio.gather(*tasks)


if __name__ == '__main__':
    a1 = sync_calc(numbers)               # Время выполнения синхронной функции sync_calc: 0.905863 сек.
    a2 = asyncio.run(main2(numbers))      # Время выполнения асинхронной функции main2: 1.248427 сек.
