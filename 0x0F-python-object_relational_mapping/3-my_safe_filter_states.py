#!/usr/bin/python3
"""filter search state by command line arg with sqlinjection guard"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    # execute SQL query
    cur.execute(
        "SELECT id, name FROM states WHERE name LIKE %s\
                ORDER BY states.id ASC;", (sys.argv[4],))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
