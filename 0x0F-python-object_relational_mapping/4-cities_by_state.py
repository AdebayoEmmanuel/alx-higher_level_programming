#!/usr/bin/python3
"""Connect db and query all cities in ascending order of id"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    # execute SQL query
    cur.execute("SELECT cities.id, cities.name, states.name\
            FROM states\
            JOIN cities ON cities.state_id=states.id\
            ORDER BY cities.id ASC;")
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
