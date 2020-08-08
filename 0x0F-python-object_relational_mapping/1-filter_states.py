#!/usr/bin/python3
"""Show lists all states with a name starting with N (upper N)."""
import MySQLdb
from sys import argv

# connect to db
if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )

    # Getting a cursor in MySQLdb python
    cur = conn.cursor()

    # Executing db queries where nama starting in N or n
    cur.execute("SELECT * FROM states WHERE name like 'N%' ORDER by id ASC")
    # Obtaining all result of queries
    query_table = cur.fetchall()
    # Printing the result one to one only if starting N
    for row in query_table:
        if row[1][0] == 'N':
            print(row)

    # Close conection to cursor and db
    cur.close()
    conn.close()
