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
    # Find the difference between the number of total points of the 'Ferrari' car team and the
    # 'Mercedes' car team. The result should contain one cell with the result called “diff”.
    cursor.execute("""
SELECT ABS( -- Calculate the absolute value of the teams' points difference
    (SELECT SUM(teams.PTS) -- Get the sum of points of the Ferrari team
     FROM teams
     WHERE teams.Team='Ferrari'
     GROUP BY teams.Team) -
    (SELECT SUM(teams.PTS) -- Get the sum of points of the Mercedes team
     FROM teams
     WHERE teams.Team='Mercedes' 
     GROUP BY teams.Team))
     AS 'diff'
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))