import sqlite3
import asyncio

import aiosqlite3

async def f():
    async with aiosqlite3.connect('mydb.db') as db:
        await db.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')


asyncio.run(f())

