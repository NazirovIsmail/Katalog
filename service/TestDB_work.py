import unittest
import asyncpg
import time
from db_work import get_all_documents,get_document, get_katalog_info

async def connection():
    conn=await asyncpg.connect(user='admin', password='admin',
                                 database='katalog', host='postgres', port=5432)
    return conn

class TestDB_work(unittest.TestCase):
    
    async def test_get_all_documents(self):
        conn=await connection()
        result=await get_all_documents(conn)
        self.assertNotEqual(result,{})

    async def test_get_document_wrong_path(self):
        conn=await connection()
        result=await get_document(conn,'111','any')
        self.assertEqual(result,'wrong request')

    async def test_get_document_nothing_found(self):
        conn=await connection()
        result=await get_document(conn,'movie_reviews','any')
        self.assertEqual(result,'Nothing found. Maybe wrong document name')
    
    async def test_get_document(self):
        conn=await connection()
        result=await get_document(conn,'games_soundtracks/Forza_horizon','The_Black_Keys_Lonely_Boy')
        self.assertEqual(result,{"format":"mp4","hash":"13692888","name":"The_Black_Keys_Lonely_Boy","size":539329})
    
    async def test_get_katalog_info_wrong_path(self):
        conn=await connection()
        result=await get_katalog_info(conn,'movie_reviews/any')
        self.assertEqual(result,'Wrong path')

if __name__ == "__main__":
  unittest.main()