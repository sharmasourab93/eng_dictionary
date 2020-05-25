from .db_conn import DBConn
from .browse_meaning import BrowseMeaning


class Dictionary:
    
    def lookup(self, key):
        db_connect = DBConn()
        query_result = db_connect.fetch_one(key)
        
        if query_result is None:
            mean = self.browse_meaning(key)
            db_connect.insert_data(key, mean)
            return {key: mean}
        
        else:
            return query_result
        
    def browse_meaning(self, key):
        
        browse = BrowseMeaning()
        meaning = browse.search(key)
        if meaning is not None:
            return meaning
        elif meaning is None:
            return None
        else:
            return "Connection to host failed."
