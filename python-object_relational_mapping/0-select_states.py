#!/usr/bin/python3
"""Script that retrieves data by id from hbtn_0e_0_usa"""


import MySQLdb
import sys


def main():
    """Get states from hbtn_0e_0_usa by id"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=db_name)
    cursor = db.cursor()
    result = cursor.execute("SELECT * FROM hbtn_0e_0_usa.states")
    cursor.close()
    return result


if __name__ == "__main__":
    main()
