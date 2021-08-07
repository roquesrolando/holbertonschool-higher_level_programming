#!/usr/bin/python3
"""List the state"""
import sys
import MySQLdb

user = sys.argv[1]
passwd = sys.argv[2]
database = sys.argv[3]
state = sys.argv[4]
db = MySQLdb.connect('localhost', user, passwd, database, 3306)
c = db.cursor()
c.execute("""SELECT * FROM states WHERE name = %(state)s
                ORDER BY id ASC""", {'state': state})
rows = c.fetchall()
for row in rows:
    print(row)
c.close()
db.close()
