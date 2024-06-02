
import asyncio
import asyncpg
import time

async def main():
    while True:
        try:
            conn = await asyncpg.connect(user='admin', password='admin',
                                        database='katalog', host='postgres', port=5432)
        except:
            time.sleep(2)
            continue
        break
    values = await conn.fetch(
        'SELECT * FROM katalog WHERE id = $1',
        1,
    )
    print(values)
    await conn.close()


if __name__ == '__main__':
    asyncio.run(main())