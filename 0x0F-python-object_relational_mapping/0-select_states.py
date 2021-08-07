#!/usr/bin/python3
import sys
import MySQLdb

db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
result = db.cursor()
result.execute("SELECT states.id, states.name FROM states
               ORDER BY states.id ASC")
myRow = result.fetchall()
for row in myRow:
    print(row)
db.close()
