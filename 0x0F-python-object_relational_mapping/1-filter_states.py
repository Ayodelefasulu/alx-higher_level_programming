#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.

Usage:
    ./1-filter_states.py <username> <password> <database_name>

Example:
    ./1-filter_states.py root root hbtn_0e_0_usa
"""

import MySQLdb
import sys

def filter_states(username, password, database_name):
    try:
        # connect to mysql server
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )

        # create a cursor object
        cur = db.cursor()

        # execute sql queries to filter states starting with 'N'
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

        # this fetches the queries selected above
        rows = cur.fetchall()

        # display the result
        for row in rows:
            print(row)

        # close the cursor and connection
        cur.close()
        db.close

    except MySQLdb.Error as e:
        print("Error connecting to database:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py\
            <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    filter_states(username, password, database_name)
