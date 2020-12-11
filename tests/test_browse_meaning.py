from unittest import TestCase, main
from unittest.mock import patch, Mock
from dictionary import BrowseMeaning
import requests
from constants import HTTP_HEADER, TAG, CLASS, PARSER
from bs4 import BeautifulSoup as Bs


class TestBrowseMeaning(TestCase):
    
    def setUp(self):
        self.rword = 'precious'
        self.url = 'https://dictionary.cambridge.org/' \
                   'dictionary/english/'
        
    @patch('dictionary.browse_meaning.get')
    @patch('dictionary.BrowseMeaning.request_word')
    def test_request_word(self, mock_obj, get):
        mock_obj.return_value = Mock(return_value=get(self.rword))
        class_ = BrowseMeaning()
        result_1 = class_.request_word(self.rword)
        self.assertEqual(mock_obj.return_value, result_1)
        
    @patch('dictionary.BrowseMeaning.extract_word')
    def test_extract_word(self, mock_obj):
        data = Mock(return_value=requests.get(self.url + self.rword,
                                              headers=HTTP_HEADER))
        soup = Mock(return_value=Bs(data.return_value.text,
                                    PARSER))
        soup = Mock(return_value=soup.find(TAG,
                                           {"class": CLASS})
                    .get_text())
        mock_obj.return_value = Mock(return_value=soup.return_value)
        
        class_ = BrowseMeaning()
        result_1 = class_.extract_word(self.rword)
        self.assertEqual(mock_obj.return_value, result_1)
        
    @patch('dictionary.BrowseMeaning.extract_word')
    @patch('dictionary.BrowseMeaning.search')
    def test_search(self, mock_obj, word_getter):
        mock_obj.return_value = Mock(return_value=
                                     word_getter.return_value)
        class_ = BrowseMeaning()
        result = class_.search(self.rword)
        self.assertEqual(mock_obj.return_value, result)
        

if __name__ == '__main__':
    main()
