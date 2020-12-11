from requests import get
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as Bs
from constants import TAG, CLASS, HTTP_HEADER, PARSER


class BrowseMeaning:
    """
    Uses request to open the url and
    bs4 for parsing the innerHTML of the webpage
    """
    
    def __init__(self):
        self.word = None
        self.url = 'https://dictionary.cambridge.org/' \
                   'dictionary/english/'
        
    def request_word(self, key):
        
        self.url += str(key)

        try:
            raw_data = get(self.url, headers=HTTP_HEADER)
            return raw_data

        except ConnectionError as e:
            raise ConnectionError("Connection Error")
        
    def extract_word(self, key):
    
        try:
            raw_data = self.request_word(key)
            soup = Bs(raw_data.text, PARSER)
        
            # Soup method to extract the
            # meaning from the tag
            get_data = soup.find(TAG,
                                 {"class": CLASS}).get_text()
            self.word = get_data
            
            return self.word
    
        except AttributeError:
            return None

    def search(self, key):
        """
        Searching the meaning on the
        Cambridge on Cambridge University site.
        """
        
        result = self.extract_word(key)
        
        return result
