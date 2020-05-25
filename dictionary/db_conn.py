import sqlite3
from .constants import CREATE_TABLE, INSERT_IN_TABLE


class DBConn:
    """ SQLite Database operations """
    
    def __init__(self):
        self.db = self.connect()
        self.db_iterator = self.db.cursor()
        self.create_table()
    
    def connect(self):
        self.db = sqlite3.connect("dict.db")
        return self.db
        
    def close(self):
        self.db.close()
    
    def create_table(self):
        """Create a table. If it exists just pass."""
        
        try:
            self.db_iterator.execute(CREATE_TABLE)
        except sqlite3.OperationalError:
            pass
    
    def insert_data(self, key, meaning):
        """Insert into table when a new key instance was found."""
        self.db_iterator.execute(INSERT_IN_TABLE, (key, meaning))
        self.db.commit()
    
    def fetch_one(self, key):
        """ Query the DB for the word and its meaning. """
        try:
            item = self.db_iterator.execute("SELECT meaning from Dictionary "
                                            "where word='{}';".format(key))
            fetch_word = item.fetchone()
            if isinstance(fetch_word, type(None)):
                raise TypeError
            else:
                return {key: str(fetch_word)}
        
        except TypeError:
            return None
    
    def fetchall(self):
        """Query all items in db"""
        try:
            item = self.db_iterator.execute("SELECT * from Dictionary;")
            new_item = dict(item.fetchall())
            return new_item
        
        except TypeError:
            return None
    
    def __exit__(self):
        """On exit commit & close."""
        self.db.commit()
        self.close()
