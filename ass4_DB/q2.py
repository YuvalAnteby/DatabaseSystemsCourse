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
-- Q2: Retrieve players drafted after 2010 who average more than 20 points per game.
SELECT player_id, player_name, AVG(points_per_game) AS avg_pts
FROM PlayerStatistics
JOIN Teams
	ON PlayerStatistics.team = Teams.team
WHERE Teams.draft_year > 2010
GROUP BY player_id
HAVING avg_pts > 20
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))