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
-- Q5: List all players from a specific conference (e.g., "").
SELECT player_id, player_name, team_conference
FROM PlayerStatistics
JOIN Teams
	ON PlayerStatistics.team = Teams.team
WHERE team_conference = 'East'
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))