import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yuval2001",
        database="basket_ball_players_statistics",
        port='3307',
    )
    cursor = mydb.cursor()
    query = """
-- Q1: Find the total points scored by players in each team.
SELECT team, SUM(points_per_game)
FROM PlayerStatistics
GROUP BY team
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))