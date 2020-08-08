#!/usr/bin/python3
"""Make join between cities and states and show speficic colum."""
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
    # Build string for make query selecting speficic colunm
    query = "SELECT cities.id, cities.name, states.name\
            FROM cities\
            INNER JOIN states\
            ON cities.state_id=states.id"
    # Getting a cursor in MySQLdb python
    cur = conn.cursor()
    # Executing db queries where nama starting in N or n
    cur.execute(query)
    # Obtaining all result of queries
    query_table = cur.fetchall()
    # Printing the result one to one only if starting arg[4]
    for row in query_table:
        print(row)
    # Close conection to cursor and db
    cur.close()
    conn.close()
