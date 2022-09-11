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
            WHERE states.name LIKE %s\
            ORDER BY cities.id ASC;", (sys.argv[4],))

    cities_list = []
    city_output = ""
    # put all cities inside list
    for row in cur.fetchall():
        cities_list.append(row[1])

    # pretty printing please be a better dev than me
    # find a better way to print out citis!
    for city in cities_list:
        city_output = city_output + str(city)
        if city is not cities_list[len(cities_list)-1]:
            city_output = city_output + ', '
    print(city_output)

    cur.close()
    db.close()
