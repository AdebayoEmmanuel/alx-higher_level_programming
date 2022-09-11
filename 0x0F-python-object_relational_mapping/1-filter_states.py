#!/usr/bin/python3
"""filter states starting with N, ordered by state id"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    # execute SQL query
    cur.execute(
        "SELECT id, name FROM states WHERE name LIKE 'N%'\
                ORDER BY states.id ASC;")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
