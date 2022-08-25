#!/usr/bin/python3
'''
Script that lists all states from the database
'''


import MySQLdb
from sys import argv

if __name__ == "__main__":
    cont = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursor = cont.cursor()
    SELECT_STATE = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC;"
    cursor.execute(SELECT_STATE, (argv[4],))
    db = cursor.fetchall()
    for i in db:
        if i[1] == argv[4]:
            print(i)
    cursor.close()
