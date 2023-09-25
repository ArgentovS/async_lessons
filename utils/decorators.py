import asyncio
import time
from functools import wraps


def timeit(func):
    """
    Декоратор для измерения времени работы асинхронной и синхронной функции.
    """
    if asyncio.iscoroutinefunction(func):
        @wraps(func)
        async def measure_time(*args, **kw):
            start_time = time.time()
            result = await func(*args, **kw)
            print(f'_____________\n'
                  f'Время выполнения асинхронной функции {func.__qualname__}:'
                  f' {(time.time() - start_time):.6f} сек.\n')
            return result
    else:
        @wraps(func)
        def measure_time(*args, **kw):
            start_time = time.time()
            result = func(*args, **kw)
            print(f'_____________\n'
                  f'Время выполнения синхронной функции {func.__qualname__}:'
                  f' {(time.time() - start_time):.6f} сек.\n')
            return result

    return measure_time
