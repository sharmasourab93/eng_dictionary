# A Naive Implementation of an English Dictionary with Databases
import urllib.request as ur
import urllib as u
import time as t
from bs4 import BeautifulSoup as bs
import sqlite3
import socket

def connect():
    try:
        s=socket.create_connection((socket.gethostbyname("www.google.com"),80),2)
        return True
    except:
        pass
    return False

class MeaningVar:
        def __init__(self):
                self.boolean=False
                self.meaning_data=''

class BrowseMeaning:
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
                        	#print("No Internet.Waiting for Connection")
                        	t.sleep(10)
                        	self.search()

class DictDB:
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

class Dictionaire:
	def __init__(self,key):
		self.key=key
		self.l=self.declareDB()
		self.lookup_Browse()
	def declareDB(self):
		db=DictDB()
		return db
	def browse(self):
		surf=BrowseMeaning(self.key)
		return surf
	def lookup_Browse(self):
		x=self.l.lookup_db(self.key)
		if x is not None:
			x=','.join(str(i) for i in x if i>='a' or i<='z')
			print('* '+x)
		else:
			y=self.browse()
			if y.word.boolean==True:
				print('^ '+y.word.meaning_data)
				self.l.insert_data(self.key,y.word.meaning_data)
			elif y.word.boolean==False:
				print("No meaning found!")

def mean(key):
    return Dictionaire(key)
