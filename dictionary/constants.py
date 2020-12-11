TAG = "div"
CLASS = "def ddef_d db"
PARSER = 'html.parser'
CREATE_TABLE = "CREATE TABLE Dictionary" \
               "(word text primary key," \
               "meaning text);"
INSERT_IN_TABLE = "INSERT into Dictionary (word, meaning) " \
                  "VALUES(?, ?)"
DESCRIBE = "describe dictionary"
SELECT_ONE = "SELECT meaning from Dictionary where word={0};"
HTTP_HEADER = {"User-Agent": "Mozilla/5.0"}
