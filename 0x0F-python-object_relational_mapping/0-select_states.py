#!/usr/bin/python3

"""Script that lists all states from the database hbtn_0e_0_usa:"""

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
                               password=password,
                               db=db,
                               charset="utf8")
        cur = conn.cursor()

        cur.execute("SELECT * FROM states ORDER BY id ASC")
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

        cur.close()
        conn.close()
