from requests import get
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as Bs
from .constants import TAG, CLASS


class BrowseMeaning:
    """
    Uses request to open the url and
    bs4 for parsing the innerHTML of the webpage
    """
    
    def __init__(self):
        self.word = None
    
    def search(self, key):
        """
        Searching the meaning on the
        Cambridge on Cambridge University site.
        """
        url = 'http://dictionary.cambridge.org/dictionary/english/' +\
              str(key)
        
        try:
            raw_data = get(url)
            soup = Bs(raw_data.text, 'html.parser')
            
            # Soup method to extract the
            # meaning from the tag
            get_data = soup.find(TAG,
                                 {"class": CLASS})\
                .get_text()
            
            self.word = get_data
            return self.word
        
        except AttributeError:
            return None
        
        except ConnectionError as e:
            raise ConnectionError("Connection Error")
