#A Beautiful Soup based English Dictionary 

An English Dictionary Implementation to explore Databases in depth.
The main method extracts the meaning of the word from the Cambridge Univ.site, if the meaning doesn't exist in the dictionary database.
After parsing from the site, it prints the meaning and inserts it into the dictionary database.
Once the meaning has been inserted into the dictionary database, look up takes O(1) time.

##Direction to install: 

	Download the package or on the command line type 
		```pip install eng-dictionary```
	After successful installation,On the Python shell :
		```python
		>>>import dictionary
		>>>obj = dictionary.Dictinary()
		>>>print(obj.lookup('<word you want to look up meaning for>')
		```

###Used the following Python modules :

	1. requests : To fetch the resources from Cambridge university url for Word meaning
	2. bs4: To parse the innerHTML for the word's meaning from the Cambridge University site 
	3. sqlite3: To lookup for the meaning of the word in the database if it exists else, for parsing and inserting into the database

###References for building the package: 
[Packaging Python](https://packaging.python.org/tutorials/packaging-projects/)