import redis


class ConnectRedis:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connect()
        
    def connect(self):
        self.redis = redis.Redis(host=self.host,
                                 port=self.port)
    
    def insert_data(self, key, value):
        """Insert the key and value for a new entry"""
        
        if key and value:
            self.redis.set(key, value)
    
    def fetch_one(self, word):
        """Fetch value for the provided key"""
        
        meaning = self.redis.get(word)
        
        if meaning is not None:
            return meaning.decode()
        
        return meaning
    
    def fetchall(self):
        """Fetch all key value pairs"""
        
        get_ = self.redis.keys('*')
        all_ = {i.decode(): self.redis.get(i).decode
                for i in get_}
        return all_
    
    def __exit__(self):
        """ On exit save and then close """

        self.redis.save()
