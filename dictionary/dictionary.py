from .redis_extension import ConnectRedis
from .browse_meaning import BrowseMeaning


class Dictionary:
    # Dictionary Object with Redis extension needs
    # a host and a port argument to connect with a
    # redis server and perform the relevant redis ops.
    def __init__(self, host, port):
        self.redis = ConnectRedis(host, port)
    
    def lookup(self, key):
        """Looks up for the word's meaning in the redis-server"""
        
        result = self.redis.fetch_one(key)
        
        if result is None:
            mean = self.browse_meaning(key)
            self.redis.insert_data(key, mean)
            return {key: mean}
        
        else:
            return {key: result}
        
    def browse_meaning(self, key):
        """Browse Meaning of the word"""
        
        browse = BrowseMeaning()
        meaning = browse.search(key)
        
        if meaning is not None:
            return meaning
        
        elif meaning is None:
            return None
        
        else:
            return "Connection to host failed."
