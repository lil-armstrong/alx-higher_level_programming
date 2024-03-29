#!/usr/bin/python3
"""Filter states by user input

display all values in the states table of hbtn_0e_0_usa that matches name
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    args = sys.argv[1:]

    if (len(args) != 4):
        print(str("Usage: {} <mysql username> " +
                  "<mysql password> " +
                  "<database name> " +
                  "<state name searched>").format(sys.argv[0]))

    else:
        [user, password, db, search] = args

        conn = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=user,
                               password=password,
                               db=db,
                               charset="utf8")
        cur = conn.cursor()
        query = str("SELECT * FROM states " +
                    "WHERE name LIKE BINARY '{}' " +
                    "ORDER BY id ASC").format(search)
        cur.execute(query)

        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

        cur.close()
        conn.close()
