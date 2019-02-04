""" A BS4 based English Dictionary Implementation with Databases"""

import sqlite3
import time as t
import urllib
import urllib.request as ur
from bs4 import BeautifulSoup as Bs


class MeaningVar:
				""" Data Structure of the Word and fetched Meaning """
				
				def __init__(self):
								self.boolean = False
								self.meaning_data = str()


class BrowseMeaning:
				""" Uses urllib for to open the url and bs4 for parsing the innerHTML of the webpage """
				
				def __init__(self, key):
								self.key = key
								self.word = self.mean
								self.search()
				
				@property
				def mean(self):
								return MeaningVar()
				
				def search(self):
								""" Searching the meaning on the Cambridge on Cambridge University site. """
								
								try:
												url = 'http://dictionary.cambridge.org/dictionary/english/' + str(self.key)
												rawdata = ur.urlopen(ur.Request(url)).read()
												soup = Bs(rawdata, 'html.parser')
												
												try:
																get_data = soup.find("p", {"class": "def-head semi-flush"}).get_text()
																self.word.boolean = True
																self.word.meaning_data = get_data
																return self.word
												
												except AttributeError:
																#print("No Meaning Found!")
																return None
												
								except urllib.error.URLError:
												
												try:
																t.sleep(10)
																self.search()
																
												except urllib.error.URLError.socket.gaierror:
																#No Internet connection
																t.sleep(10)
																self.search()


class DictDB:
				""" SQLite Database operations """
				
				def __init__(self):
								self.db = sqlite3.connect("dict.db")
								self.db_iterator = self.db.cursor()
				
				def insert_data(self, key, meaning):
								try:
												self.db_iterator.execute('''CREATE TABLE Dictionary (word text primary key,meaning text)''')
												
								except sqlite3.OperationalError:
												pass
								
								self.db_iterator.execute('''INSERT into Dictionary (word,meaning) VALUES(?,?)''', (key, meaning))
								self.db.commit()
				
				def lookup_db(self, key):
								""" Query the DB for the word and its meaning. """
								
								self.db = sqlite3.connect("dict.db")
								self.db_iterator = self.db.cursor()
								try:
												self.db_iterator.execute('''SELECT meaning from Dictionary where word= (?)''', (key,))
												fetchword = self.db_iterator.fetchone()
												return fetchword
								
								except sqlite3.OperationalError:
												return None


class Dictionary:
				""" Main class which handles the other two class and STDOUT the result i.e. meaning of a word"""
				
				def __init__(self, key):
								""" Constructor function to handle all the prime functions of the class """
								
								self.key = key.lower()
								self.dbconnect = DictDB()
								self.lookup_browse()
				
				def browse(self):
								surf = BrowseMeaning(self.key)
								return surf
				
				@staticmethod
				def washing_string(string):
								""" To remove unwanted characters in the string """
								
								string_set = {'A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2', ':', '›', '[', ']'}
								string = string.strip()
								for i in string_set:
												if i in string:
																string = string.replace(i, '')
								string = string.capitalize()
								return string
				
				def lookup_browse(self):
								query_result = self.dbconnect.lookup_db(self.key)
								if query_result is not None:
												query_result = ','.join(str(i) for i in query_result if i >= 'a' or i <= 'z')
												print(query_result)
								else:
												y = self.browse()
												if y.word.boolean:
																w = self.washing_string(y.word.meaning_data)
																print(w)
																self.dbconnect.insert_data(self.key, w)
												elif not y.word.boolean:
																print("No meaning found!")


def mean(key):
				Dictionary(key)
