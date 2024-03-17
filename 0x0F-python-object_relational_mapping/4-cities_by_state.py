#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )

        # create cursor
        cursor = db.cursor()

        # execute query
        query = "SELECT cities.id, cities.name, states.name " \
                 "FROM cities " \
                 "JOIN states ON cities.state_id = states.id " \
                 "ORDER BY cities.id ASC;"

        cursor.execute(query)

        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(row)
        # else:
            # print()

        # close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb as e:
        print("Connection could not be established", e)
        sys.exit(1)

        
