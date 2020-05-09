TAG = "div"
CLASS = "def ddef_d db"
TABLE_NAME = 'Dictionary'
CREATE_TABLE = "CREATE TABLE {}" \
               "(word text primary key," \
               "meaning text);".format(TABLE_NAME)
INSERT_IN_TABLE = "INSERT into {}} (word, meaning) " \
                  "VALUES(?, ?)".format(TABLE_NAME)
