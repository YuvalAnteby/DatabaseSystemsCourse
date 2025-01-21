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
-- Q8: Find the average points per game for players grouped by team and position, filtered by draft year.
SELECT ps.team, pp.position, AVG(points_per_game)
FROM PlayerStatistics AS ps
JOIN PlayerPositions AS pp
	ON ps.player_name = pp.player_name
JOIN Teams AS t
	ON ps.team = t.team
WHERE t.draft_year > 2014
GROUP BY ps.team, pp.position
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))