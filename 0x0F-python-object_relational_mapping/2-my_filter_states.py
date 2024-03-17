#!/usr/bin/python3
"""
Script that takes an argument and displays all values...
   in the states table of hbtn_0e_0_usa where name matches the argument.

Usage:
    ./2-my_filter_states.py <username> <password> <database_name> <state_name>

Example:
    ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
"""

import MySQLdb
import sys


def filter_states(username, password, database_name, state_name):
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

        # Execute SQL query to filter states based on provided state name
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"\
            .format(state_name)
        cursor.execute(query)

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
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py\
            <username> <password> <database_name> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    filter_states(username, password, database_name, state_name)
