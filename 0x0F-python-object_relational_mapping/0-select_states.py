#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.

Usage:
    ./0-select_states.py <username> <password> <database_name>

Example:
    ./0-select_states.py root root hbtn_0e_0_usa
"""

import MySQLdb
import sys


def get_states(username, password, database_name):
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )

        # Create a cursor object
        cursor = db.cursor()

        # Execute the SQL query
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

        # Close the cursor and connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <username>\
            <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    get_states(username, password, database_name)
