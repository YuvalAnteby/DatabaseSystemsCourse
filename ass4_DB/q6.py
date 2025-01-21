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
-- Q6: Find players with more than 20 points per game from a specific team drafted after a given year.
SELECT player_id, player_name, points_per_game, draft_year, Teams.team
FROM PlayerStatistics
JOIN Teams
	ON PlayerStatistics.team = Teams.team
WHERE draft_year > 2013
AND points_per_game > 20
AND PlayerStatistics.team = 'Bulls'
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))