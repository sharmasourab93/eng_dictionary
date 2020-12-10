TAG = "div"
CLASS = "def ddef_d db"
CREATE_TABLE = "CREATE TABLE Dictionary" \
               "(word text primary key," \
               "meaning text);"
INSERT_IN_TABLE = "INSERT into Dictionary (word, meaning) " \
                  "VALUES(?, ?)"
HTTP_HEADER = {"User-Agent": "Mozilla/5.0"}
