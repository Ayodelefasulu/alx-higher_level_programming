#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa.

Usage:
    ./5-filter_cities.py <username> <password> <database_name> <state_name>

Example:
    ./5-filter_cities.py root root hbtn_0e_4_usa Texas
"""

import MySQLdb
import sys


# Check if the script is being executed directly
if __name__ == "__main__":
    # Verify that the correct number of command-line arguments are provided
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py\
            <username> <password> <database_name> <state_name>")
        sys.exit(1)  # Exit with an error code if arguments are incorrect

    # Assign command-line arguments to variables
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to MySQL server using the provided credentials
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )

        # Create a cursor object to execute SQL queries
        cursor = db.cursor()

        # Use a parameterized query to filter cities by state name
        query = "SELECT cities.name FROM cities " \
                "JOIN states ON cities.state_id = states.id " \
                "WHERE states.name = %s ORDER BY cities.id ASC"

        cursor.execute(query, (state_name,))

        # Fetch all the rows from the query result
        rows = cursor.fetchall()

        # Display the filtered cities
        if rows:
            cities = ', '.join(row[0] for row in rows)
            print(cities)
        else:
            print("No cities found for the state:", state_name)

        # Close the cursor and MySQL connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        # Handle MySQL errors and print an error message
        print("Error connecting to MySQL:", e)
        sys.exit(1)  # Exit with an error code if there is a MySQL error
