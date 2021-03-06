#!/usr/bin/python3
"""List all states from a specified database"""
import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect('localhost', user, passwd, database, 3306)
    c = db.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name
            FROM cities JOIN states
            ON states.id = cities.state_id
            ORDER BY cities.id""")
    rows = c.fetchall()
    for row in rows:
        print(row)
    db.close()
