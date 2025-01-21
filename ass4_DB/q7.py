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
-- Q7: Retrieve the total points scored (games_played × points_per_game) 
-- for each position within a specific team.
SELECT position, SUM(games_played * points_per_game)
FROM PlayerStatistics
JOIN PlayerPositions
	ON PlayerStatistics.player_name = PlayerPositions.player_name
WHERE team = 'lakers'
GROUP BY position
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))