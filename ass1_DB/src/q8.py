import mysql.connector
if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="f1_data",
        port='3307',
    )
    cursor = mydb.cursor()
    cursor.execute("""
        SELECT ABS(
            (SELECT     SUM(teams.PTS)
            FROM        teams
            WHERE       teams.Team='Ferrari'
            GROUP BY    teams.Team)-
            (SELECT     SUM(teams.PTS)
            FROM        teams
            WHERE       teams.Team='Mercedes'
            GROUP BY    teams.Team))
        AS 'diff'
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))