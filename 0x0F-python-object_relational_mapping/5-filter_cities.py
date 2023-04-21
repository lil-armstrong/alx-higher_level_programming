#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """

if __name__ == '__main__':
    import MySQLdb
    import sys

    args = sys.argv[1:]

    if (len(args) != 4):
        raise ValueError(
            str("Usage: {} <user> " +
                "<password> " +
                "<db> <state>").format(sys.argv[0]))

    [user, password, db, state] = args

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=user,
                           password=password,
                           db=db,
                           charset="utf8")
    cur = conn.cursor()

    query = str("SELECT cities.name as name, " +
                "FROM cities " +
                "INNER JOIN states ON cities.state_id=states.id " +
                "WHERE states.name=%s " +
                "ORDER BY cities.id ASC;")
    # print(query)
    cur.execute(query, (state, ))

    query_rows = cur.fetchall()
    tmp = list(row[0] for row in query_rows)
    print(*tmp, sep=", ")

    cur.close()
    conn.close()
