# A BS4 based English Dictionary Implementation with Databases
import urllib.request as ur
import urllib as u
from bs4 import BeautifulSoup as bs
import time as t
import sqlite3

class MeaningVar:
    """ Data Structure of the Word and fetched Meaning """
    def __init__(self):
        self.boolean=False
        self.meaning_data=str()

class BrowseMeaning:
    """ Uses urllib for to open the url and bs4 for parsing the innerHTML of the webpage """

    def __init__(self,key):
        self.key=key
        self.word=self.mean()
        self.search()

    def mean(self):
        return MeaningVar()

    def search(self):
        try:
            url='http://dictionary.cambridge.org/dictionary/english/'+str(self.key)
            rawdata=ur.urlopen(ur.Request(url)).read()
            soup=bs(rawdata,'html.parser')
            try:
                get_data=soup.find("p",{"class":"def-head semi-flush"}).get_text()
                self.word.boolean=True
                self.word.meaning_data=get_data
                return self.word
            except AttributeError:
                #print("No Meaning Found!")
                return None
        except u.error.URLError:
            try:
                t.sleep(10)
                self.search()
            except u.error.URLError.socket.gaierror:
                #No Internet connection
                t.sleep(10)
                self.search()

class DictDB:
    """ SQLite Database operations """

    def __init__(self):
        self.db=sqlite3.connect("dict.db")
        self.iterator=self.db.cursor()

    def create_table(self):
        self.iterator.execute('''CREATE TABLE Dictionary (word text primary key,meaning text)''')

    def insert_data(self,key, meaning):
        try:
            self.create_table()
        except sqlite3.OperationalError:
            pass
        self.iterator.execute('''INSERT into Dictionary (word,meaning) VALUES(?,?)''',(key,meaning))
        self.db.commit()

    def lookup_db(self,key):
        self.db=sqlite3.connect("dict.db")
        self.iterator=self.db.cursor()
        try:
            self.iterator.execute('''SELECT meaning from Dictionary where word= (?)''',(key,))
            fetching=self.iterator.fetchone()
            return fetching
        except sqlite3.OperationalError:
            return None

class dictionary:
    """ Main class which handles the other two class and STDOUT the result i.e. meaning of a word"""
    
    def __init__(self,key):
        self.key=key.lower()
        self.l=DictDB()
        self.lookup_Browse()

    def browse(self):
        surf=BrowseMeaning(self.key)
        return surf

    def washing_String(self,string):
        string_set={'A1','A2','B1','B2','C1','C2','D1','D2',':','›','[',']'}
        string=string.strip()
        for i in string_set:
            if i in string:
                string=string.replace(i,'')
        string=string.capitalize()
        return string
    
    def lookup_Browse(self):
        x=self.l.lookup_db(self.key)
        if x is not None:
            x=','.join(str(i) for i in x if i>='a' or i<='z')
            print(x)
        else:
            y=self.browse()
            if y.word.boolean==True:
                w=self.washing_String(y.word.meaning_data)
                print(w)
                self.l.insert_data(self.key,w)
            elif y.word.boolean==False:
                print("No meaning found!")
def mean(key):
    dictionary(key)
