#!/usr/bin/python3
import sys
'''
a script that lists all states from the database hbtn_0e_0_usa
'''
MY_HOST=sys.argv[1]
MY_USER=sys.argv[2]
MY_PASS=sys.argv[3]
MY_DB=sys.argv[4]
e
db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)

