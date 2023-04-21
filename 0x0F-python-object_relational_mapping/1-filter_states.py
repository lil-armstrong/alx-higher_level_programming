#!/usr/bin/python3
"""list all states with a name starting with N (upper N) from hbtn_0e_0_usa"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    args = sys.argv[1:]

    if (len(args) != 3):
        print(str("Usage: {} <mysql username> " +
                  "<mysql password> " +
                  "<database name>").format(
            sys.argv[0]))

    else:
        [user, password, db] = args

        conn = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=user,
                               passwd=password,
                               db=db,
                               charset="utf8")
        cur = conn.cursor()

        cur.execute(
            str("SELECT * FROM states " +
                "WHERE name LIKE BINARY " +
                "'N%' ORDER BY states.id ASC"))
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

        cur.close()
        conn.close()
