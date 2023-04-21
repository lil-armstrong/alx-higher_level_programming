#!/usr/bin/python3


if __name__ == '__main__':
    import MySQLdb
    import sys

    args = sys.argv[1:]

    if (len(args) != 3):
        raise ValueError("Missing arguments")

    [user, password, db] = args

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=user, password=password, db=db, charset="utf8")
    cur = conn.cursor()
    query = "SELECT cities.id as id, " +\
        "cities.name as name, " +\
        "states.name as state " +\
            "FROM cities " +\
            "INNER JOIN  states ON cities.state_id=states.id " +\
            "ORDER BY cities.id ASC;"
    # print(query)
    cur.execute(query)

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
