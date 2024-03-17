#!/usr/bin/python3
"""
Safe script that filters and lists states from
    the database hbtn_0e_0_usa using parameterized queries.

Usage:
    ./2-my_filter_states.py <username> <password> <database_name> <state_name>

Example:
    ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona"
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py\
            <username> <password> <database_name> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )

        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print("No name found for this user:", state_name)

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Connection could not be established", e)
        sys.exit(1)
