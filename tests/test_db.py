from os import remove, path
from unittest import TestCase, main
from dictionary import DBConn
from sqlite3 import ProgrammingError, IntegrityError


class TestDBConn(TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        if path.exists('dict.db'):
            remove('dict.db')
    
    def setUp(self) -> None:
        self.dbconn = DBConn()
        self.key, self.word = 'precious', 'word'
        self.wrong_word = 'abcd'
        self.conn_fail = "Connection to host failed."
        self.meaning_1 = "of great value because of being " \
                         "rare, expensive, or important: "
        self.meaning = "a single unit of language that has" \
                       " meaning and can be spoken or written: "
    
    @classmethod
    def tearDownClass(cls) -> None:
        if path.exists('dict.db'):
            remove('dict.db')
    
    def test_connect_db(self):
        db_item = self.dbconn.connect()
        self.assertEqual(len(db_item.cursor().execute('SELECT * from Dictionary;').fetchall()),
                         len([]))
        
    def test_close_db(self):
        self.dbconn.close()
        item = self.dbconn.fetchall
        self.assertRaises(ProgrammingError,
                          item)
        
    def test_insert_data(self):
        query = "SELECT meaning from Dictionary where word='{}';"
        self.dbconn.insert_data(self.key, self.meaning_1)
        self.dbconn.insert_data(self.word, self.meaning)
        
        self.assertEqual(self.dbconn.db_iterator.execute(
            query.format(self.key)).fetchone(), (self.meaning_1,))
        self.assertEqual(self.dbconn.db_iterator.execute(
            query.format(self.word)).fetchone(), (self.meaning,))
        self.assertEqual(self.dbconn.db_iterator.execute(
            query.format(self.wrong_word)).fetchone(), None)

        self.assertRaises(IntegrityError,
                          self.dbconn.insert_data,
                          self.word,
                          self.meaning)
        
    def test_fetch_one(self):
        insert = "INSERT into Dictionary (word, meaning) VALUES(?, ?)"
        
        self.dbconn.db_iterator.execute(insert, (self.key, self.meaning_1))
        self.assertEqual(self.dbconn.fetch_one(self.key)[self.key], str((self.meaning_1, )))
        self.dbconn.db_iterator.execute(insert, (self.word, self.meaning))
        self.assertEqual(self.dbconn.fetch_one(self.word)[self.word], str((self.meaning, )))

        self.assertEqual(self.dbconn.fetch_one(self.wrong_word), None)
        
    def test_fetchall(self):
        insert = "INSERT into Dictionary (word, meaning) VALUES(?, ?)"
        self.dbconn.db_iterator.execute(insert, (self.key, self.meaning_1))
        self.dbconn.db_iterator.execute(insert, (self.word, self.meaning))
        all_items = self.dbconn.fetchall()
        self.assertEqual(len(all_items), 2)
        

if __name__ == '__main__':
    main()
