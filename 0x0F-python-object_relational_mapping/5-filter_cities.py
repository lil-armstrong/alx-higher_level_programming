#!/usr/bin/python3
"""All cities by state

Takes in the name of a state as an argument and lists all cities 
of that state, using the database hbtn_0e_4_usa
"""

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

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=user, password=password, db=db, charset="utf8")
    cur = conn.cursor()

    query = str("SELECT cities.id as id, " +
                "cities.name as name, " +
                "states.name as state " +
                "FROM cities " +
                "INNER JOIN states ON cities.state_id=states.id " +
                "WHERE states.name LIKE '{}' " +
                "ORDER BY cities.id ASC;").format(state)
    # print(query)
    cur.execute(query)

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row[1], end=", ")

    cur.close()
    conn.close()
