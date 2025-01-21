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
-- Q3: List the top 5 players with the highest rebounds per game.
SELECT player_id, player_name, rebounds_per_game
FROM PlayerStatistics
ORDER BY rebounds_per_game DESC
LIMIT 5
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))