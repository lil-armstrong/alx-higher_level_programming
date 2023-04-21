#!/usr/bin/python3


if __name__ == '__main__':
    import MySQLdb
    import sys

    args = sys.argv[1:]

    if (len(args) != 4):
        raise ValueError("Missing arguments")

    [user, password, db, search] = args

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=user, password=password, db=db, charset="utf8")
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC".format(
        search)
    cur.execute(query)

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
