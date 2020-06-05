from os import remove, path
from unittest import TestCase, main
from redis_extension import ConnectRedis
import redis


class TestConnectRedis(TestCase):
    
    def setUp(self) -> None:
        self.host, self.port = '192.168.43.65', 6379
        
        try:
            # ConnectRedis Class Object
            self.redis = ConnectRedis(self.host, self.port)
            
            # Independent Redis object
            self.redis_obj = redis.Redis(host=self.host, port=self.port)
        except redis.exceptions.ConnectionError or ConnectionError:
            pass
        
        # Keys & Values to be used every often
        self.key, self.word = 'precious', 'word'
        self.wrong_word = 'abcd'
        self.conn_fail = "Connection to host failed."
        self.meaning_1 = "of great value because of being " \
                         "rare, expensive, or important: "
        self.meaning = "a single unit of language that has" \
                       " meaning and can be spoken or written: "
        
    def tearDown(self) -> None:
        try:
            self.redis_obj.flushall()
        except redis.exceptions.ConnectionError or ConnectionError:
            pass
    
    def test_connect(self):
        try:
            if redis.Redis(host=self.host, port=self.port).ping():
                self.assertTrue("Connection established.")
                
        except redis.exceptions.ConnectionError or ConnectionError:
            self.assertRaises(redis.exceptions.ConnectionError)
        
    def test_insert_data(self):
        try:
            
            self.redis.insert_data(self.key, self.meaning_1)
            self.redis.insert_data(self.word, self.meaning)
            
            for_key = self.redis_obj.get(self.key).decode()
            for_word = self.redis_obj.get(self.word).decode()
            
            self.assertEqual(self.meaning_1, for_key)
            self.assertEqual(self.meaning, for_word)
        
        except redis.exceptions.ConnectionError or ConnectionError:
            self.assertRaises(redis.exceptions.ConnectionError)
    
    def test_fetch_one(self):
        try:
            
            self.redis_obj.set(self.key, self.meaning_1)
            self.redis_obj.set(self.word, self.meaning)
            self.redis_obj.save()
            
            m1 = self.redis.fetch_one(self.key)
            m2 = self.redis.fetch_one(self.word)
            
            self.assertEqual(m1, self.meaning_1)
            self.assertEqual(m2, self.meaning)
            self.assertEqual(self.redis.fetch_one(self.wrong_word), None)
        
        except redis.exceptions.ConnectionError or ConnectionError:
            self.assertRaises(redis.exceptions.ConnectionError)
        
    def test_fetchall(self):
        try:
            
            self.redis_obj.set(self.word, self.meaning)
            self.redis_obj.set(self.key, self.meaning_1)
            
            obj = self.redis.fetchall()
            self.assertEqual(len(obj), 2)
        
        except redis.exceptions.ConnectionError or ConnectionError:
            self.assertRaises(redis.exceptions.ConnectionError)
        

if __name__ == '__main__':
    main()