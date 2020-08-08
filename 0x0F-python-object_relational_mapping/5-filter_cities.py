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
    # Build string for make safety query selecting speficic colunm
    if ";" not in argv[4]:
        query = "SELECT cities.name\
                FROM cities\
                INNER JOIN states\
                ON cities.state_id=states.id\
                WHERE states.name='{}'".format(argv[4])
        # Getting a cursor in MySQLdb python
        cur = conn.cursor()
        # Executing db queries where nama starting in N or n
        cur.execute(query)
        # Obtaining all result of queries
        query_table = cur.fetchall()
        # Printing the result one to one only if starting arg[4]
        s = ""
        for row in query_table:
            print(s, end="")
            print("{}".format(row[0]), end="")
            s = ", "
        print("")
        # Close conection to cursor
        cur.close()
    # Close conection to db
    conn.close()
