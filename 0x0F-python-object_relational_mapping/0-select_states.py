#!/usr/bin/python3
"""List all states from the database"""

import sys
import MySQLdb

user, passwd, database = sys.argv[1:4]
db = MySQLdb.connect('localhost', user, passwd, database, 3306)
c = db.cursor()
c.execute("SELECT * FROM states ORDER BY id ASC")
rows = c.fetchall()
for row in rows:
    print(row)
c.close()
db.close()
