from requests import get
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as Bs
from constants import TAG, CLASS, HTTP_HEADER


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
        url = 'https://dictionary.cambridge.org/dictionary/english/' +\
              str(key)
        
        try:
            raw_data = get(url, headers=HTTP_HEADER)
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


if __name__ == '__main__':
    obj = BrowseMeaning()
    result = obj.search('precious')
    print(result)