"""
import sqlite3
conn = sqlite3.connect('mydatabase.db')

cur = conn.cursor()

# cur.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# cur.executemany('''INSERT INTO users (name,age) VALUES (?,?)''', [('abc', 20) for i in range(10)])

cur.execute('SELECT * FROM users')
# rows = cur.fetchall()
# rows = cur.fetchmany(3)
# for row in rows:
#     print(row)

conn.commit()
conn.close()
"""

import aiosqlite
import asyncio

async def main():
    async with aiosqlite.connect('mydb.db') as db:
        cur = await db.execute('SELECT * FROM users')
        rows = await cur.fetchall()
        for row in rows:
            print(row)

        

asyncio.run(main())