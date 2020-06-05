# A Beautiful Soup based English Dictionary - Using Redis Extension & Compatibility 

To explore the default `sqlite3` implementation of `eng_dictionary` visit --> [eng_dictionary](https://github.com/sharmasourab93/eng_dictionary/tree/master)

Objective is to explore [Redis](https://redis.io/) and implement it to a practical use case.

An English Dictionary Implementation using, 

        * requests 
        * bs4 
        * py-redis
    
The main method extracts the meaning of the word from the Cambridge University site, if the meaning doesn't exist in the redis server.
After parsing from the site, it prints the meaning and inserts the parsed value into the redis server.

## Direction To install & Use Components in the package: 

1. Git Clone or Download the package from the following [url](https://github.com/sharmasourab93/eng_dictionary/tree/py-redis).   
      
2. After successful installation,On the Python shell :  
    ```
        >>>import dictionary
        >>>obj = dictionary.Dictinary()
        >>>print(obj.lookup('<word you want to look up meaning for>')
    ```  
   	
3. To Use bs4 Component
    ```
       >>> from dictionary import BrowseMeaning
       >>> obj = BrowseMeaning()
       >>> print(obj.search('<word you want to browse meaning for>'))
    ```

4. To Use the redis-extension:

 
   **NOTE: It's important to have redis server installed and running to use this feature.**
   
   This extension enables you to pass host & port as arguments to the redis module and perform the following operations:  
    
        *  Insert a key & value pair (Word and it's meaning in our scenario)
        *  Fetch value for a key
        *  Fetch all entries made
        
   To use the redis module 
   
       ```python
                from redis_extension import ConnectRedis 
                redis_obj = ConnectRedis('localhost', 6379)
                redis_obj.insert('someword', 'somevalue')
                value = redis_obj.fetch_one('someword') 
                print(value) # Some value, None if the key is Null 
        ```
        
 
### Used the following Python modules :

	1. requests : To fetch the resources from Cambridge university url for Word meaning
	2. bs4: To parse the innerHTML for the word's meaning from the Cambridge University site 
	3. redis: To lookup for the meaning of the word in the database if it exists else, 
	          for parsing and inserting into the redis-server.

### References for building the package: 
[Packaging Python](https://packaging.python.org/tutorials/packaging-projects/)

### Improvements In The Previous Version
1. Extension with Flask in a separate branch and exploring it.
