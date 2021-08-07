#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa:
    - Your script should take 3 arguments: mysql username, mysql
        password and database name (no argument validation needed)
    - You must use the module MySQLdb (import MySQLdb)
    - Your script should connect to a MySQL server running on
        localhost at port 3306
    - Results must be sorted in ascending order by states.id
    - Results must be displayed as they are in the example below
"""
import sys
import MySQLdb

user = sys.argv[1]
passwd = sys.argv[2]
database = sys.argv[3]
db = MySQLdb.connect('localhost', user, passwd, database, 3306)
c = db.cursor()
c.execute("SELECT * FROM states ORDER BY id ASC")
rows = c.fetchall()
for row in rows:
    print(row)
c.close()
db.close()
