#!/usr/bin/python3
"""Script that retrieves data by id from hbtn_0e_0_usa"""


import MySQLdb
import sys


def main():
    """Get states from hbtn_0e_0_usa by id"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    result = cursor.fetchall()
    for i in result:
        print(i)
    cursor.close()


if __name__ == "__main__":
    main()
