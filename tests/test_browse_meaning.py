import socket
from unittest import TestCase, main
from unittest.mock import patch
from requests.exceptions import ConnectionError
from dictionary import BrowseMeaning


class TestBrowseMeaning(TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        self.browse = BrowseMeaning()
        self.rword = 'precious'
        self.meaning = "of great value because of being " \
                       "rare, expensive, or important: "
        self.wrong_word = 'abcd'
    
    def test_search(self):
        try:
            with patch('requests.get') as mocked_get:
                mocked_get.return_val.ok = True
                mocked_get.return_val.text = self.meaning
        
                search = self.browse.search(self.rword)
                mocked_get("https://dictionary.cambridge"
                           ".org/dictionary/english/{}"
                           .format(self.rword))
                self.assertEqual(search, self.meaning)
        
                mocked_get.return_val.ok = False
                search = self.browse.search(self.wrong_word)
                mocked_get("https://dictionary.cambridge"
                           ".org/dictionary/english/{}"
                           .format(self.wrong_word))
                self.assertEqual(search, None)
                
        except (socket.gaierror,
                ConnectionError):
            pass


if __name__ == '__main__':
    main()
