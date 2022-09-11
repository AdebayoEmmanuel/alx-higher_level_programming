#!/usr/bin/python3
import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", port=3306,
                     user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

cur = db.cursor()

# execute SQL query
cur.execute("SELECT id, name FROM states ORDER BY states.id ASC;")
for row in cur.fetchall():
    print(row)

cur.close()
db.close()
