import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yuval2001",
        database="f1_data",
        port='3307',
    )
    cursor = mydb.cursor()
    # Find the driver who won in one of the f1 contests in the year 2000, and had the most amount of laps.
    # Print his name and the minimum of his fastest lap time.
    # The answer should contain the driver name and the minimum time as “min_time”.
    query = """
-- print name & min_time, one that had the most amount of laps, in 2000, 
SELECT 	winners.Winner AS driver_name, MIN(MINUTE(STR_TO_DATE(fastest_laps.Time, '%i:%s.%f')))  AS min_time
FROM	winners
JOIN 	fastest_laps ON winners.Winner = fastest_laps.Driver
WHERE   YEAR(Date) = 2000 -- Needed year
        AND winners.Laps = (
            SELECT  MAX(winners.Laps) -- Get the one with most laps 
			FROM    winners
            WHERE   YEAR(Date) = 2000
            )
GROUP BY driver_name
ORDER BY min_time;
         """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))