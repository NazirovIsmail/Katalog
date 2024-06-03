import asyncio
import asyncpg
import time
from db_work import get_all_documents, get_document, insert_new_katalog,insert_new_document

async def main():
    while True:
        try:
            conn = await asyncpg.connect(user='admin', password='admin',
                                        database='katalog', host='postgres', port=5432)
        except:
            time.sleep(2)
            continue
        break
    await get_all_documents(conn)
    await get_document(conn,'movie reviews','Blade Runner')
    await insert_new_katalog(conn,'movie reviews/80s', 'year 83')
    await insert_new_document(conn, 'movie reviews/80s', ('Beverly Hills Cop','txt',1,2))
    await conn.close()





if __name__ == '__main__':
    asyncio.run(main())