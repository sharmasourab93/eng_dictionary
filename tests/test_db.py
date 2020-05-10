from os import remove, path
from unittest import TestCase, main
from dictionary import DBConn
from sqlite3 import OperationalError, ProgrammingError, IntegrityError


class TestDBConn(TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        if path.exists('dict.db'):
            remove('dict.db')
    
    def setUp(self) -> None:
        self.dbconn = DBConn()
    
    @classmethod
    def tearDownClass(cls) -> None:
        if path.exists('dict.db'):
            remove('dict.db')
    
    def test_connect_db(self):
        db_item = self.dbconn.connect()
        db_item.cursor().execute('SELECT * from Dictionary;')
        
    def test_close_db(self):
        self.dbconn.close()
        item = self.dbconn.fetchall
        self.assertRaises(ProgrammingError,
                          item)
        
    def test_insert_data(self):
        key_1, meaning_1 = 'precious', \
                           "of great value because of being " \
                           "rare, expensive, or important: "
        word, meaning = 'word', "a single unit of language that has" \
                                " meaning and can be spoken or written: "
        wrong_word = 'abcd'
        query = "SELECT meaning from Dictionary where word='{}';"
        self.dbconn.insert_data(key_1, meaning_1)
        self.dbconn.insert_data(word, meaning)
        
        self.assertEqual(self.dbconn.db_iterator.execute(
            query.format(key_1)).fetchone(), (meaning_1,))
        self.assertEqual(self.dbconn.db_iterator.execute(
            query.format(word)).fetchone(), (meaning,))
        self.assertEqual(self.dbconn.db_iterator.execute(
            query.format(wrong_word)).fetchone(), None)

        self.assertRaises(IntegrityError,
                          self.dbconn.insert_data,
                          word,
                          meaning)
        
    def test_fetch_one(self):
        key_1, meaning_1 = 'precious', \
                           "of great value because of being " \
                           "rare, expensive, or important: "
        word, meaning = 'word', "a single unit of language that has" \
                                " meaning and can be spoken or written: "
        wrong_word = 'abcd'
        insert = "INSERT into Dictionary (word, meaning) VALUES(?, ?)"
        
        self.dbconn.db_iterator.execute(insert, (key_1, meaning_1))
        self.assertEqual(self.dbconn.fetch_one(key_1)[key_1], str((meaning_1, )))
        self.dbconn.db_iterator.execute(insert, (word, meaning))
        self.assertEqual(self.dbconn.fetch_one(word)[word], str((meaning, )))

        self.assertEqual(self.dbconn.fetch_one(wrong_word), None)
        
    def test_fetchall(self):
        key_1, meaning_1 = 'precious', \
                           "of great value because of being " \
                           "rare, expensive, or important: "
        word, meaning = 'word', "a single unit of language that has" \
                                " meaning and can be spoken or written: "
        insert = "INSERT into Dictionary (word, meaning) VALUES(?, ?)"
        self.dbconn.db_iterator.execute(insert, (key_1, meaning_1))
        self.dbconn.db_iterator.execute(insert, (word, meaning))
        all_items = self.dbconn.fetchall()
        self.assertEqual(len(all_items), 2)
        

if __name__ == '__main__':
    main()
