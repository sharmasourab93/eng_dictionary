from dictionary import Dictionary
from unittest import TestCase, main
from os import remove, path


class TestDictionary(TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        if path.exists('dict.db'):
            remove('dict.db')
            
    def setUp(self) -> None:
        self.dict_ = Dictionary()
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
    
    def test_lookup(self):
        lookup_1 = self.dict_.lookup(self.key)
        if lookup_1[self.key] == self.conn_fail :
            self.assertEqual(lookup_1[self.key],
                             self.conn_fail)
        else:
            dict_1 = {self.key: self.meaning_1}
            self.assertEqual(lookup_1, dict_1)
            
            lookup_2 = self.dict_.lookup(self.word)
            dict_2 = {self.word: self.meaning}
            self.assertEqual(lookup_2, dict_2)
            
            lookup_3 = self.dict_.lookup(self.wrong_word)
            dict_3 = {self.wrong_word: None}
            self.assertEqual(lookup_3, dict_3)
        
    def test_browsing(self):
        browse = self.dict_.browse_meaning(self.key)
        if browse == self.conn_fail:
            self.assertEqual(browse, self.conn_fail)
        else:
            self.assertEqual(browse, self.meaning_1)
            
            browse_1 = self.dict_.browse_meaning(self.word)
            self.assertEqual(browse_1, self.meaning)
            
            browse_2 = self.dict_.browse_meaning(self.wrong_word)
            self.assertEqual(browse_2, None)


if __name__ == '__main__':
    main()
