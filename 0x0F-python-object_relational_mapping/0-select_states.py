#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve the list of states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and display the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()

