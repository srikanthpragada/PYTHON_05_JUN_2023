# Test connection

import sqlite3
import dbutil

try:
    with sqlite3.connect(dbutil.DBNAME) as con:
        print('Connection object is ', type(con))
        print("Connected Successfully!")

except Exception as ex:
    print('Error :', ex)
