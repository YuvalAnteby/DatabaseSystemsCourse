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
        SELECT      t1.Nationality, t1.avg_pts, t2.min_time, t3.latest
        FROM 
            (SELECT     drivers.Nationality, AVG(drivers.PTS) AS avg_pts
            FROM        drivers
            GROUP BY    drivers.Nationality) AS t1
        LEFT JOIN 
            (SELECT     drivers.Nationality, MIN(fastest_laps.Time) AS min_time
            FROM        fastest_laps, drivers
            WHERE       drivers.Driver = fastest_laps.Driver
            AND         TIME > '0:00.000'
            GROUP BY    drivers.Nationality) AS t2 
        ON  t1.Nationality = t2.Nationality
        LEFT JOIN 
            (SELECT     drivers.Nationality, MAX(winners.Date) AS latest
            FROM        winners, drivers
            WHERE       drivers.Driver = winners.Winner
            GROUP BY    drivers.Nationality) AS t3 
        ON  t1.Nationality = t3.Nationality
		HAVING min_time IS NOT NULL AND latest IS NOT NULL
		ORDER BY Nationality ASC
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))