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
    # Write a query such that for each nationality of the drivers, will find:
    # a. The average points of all drivers from each nationality
    # b. The minimum fastest laps from each country ever
    # c. The latest date where this nationality won an F1 race
    # d. Note: The answer should contain the Nationality, the average of points as
    # “avg_pts”, the fastest lap time as “min_time” and the last date as “latest”
    cursor.execute("""
SELECT 
    t1.Nationality, 
    t1.avg_pts, 
    t2.min_time, 
    t3.latest
FROM 
        (SELECT -- Get the average points grouped by nationalities of drivers
            drivers.Nationality, 
            AVG(drivers.PTS) AS avg_pts
        FROM drivers
        GROUP BY drivers.Nationality) AS t1
LEFT JOIN 
        (SELECT -- Get the fastest lap grouped by nationalities of drivers
            drivers.Nationality, 
            MIN(fastest_laps.Time) AS min_time
        FROM fastest_laps, drivers
        WHERE drivers.Driver = fastest_laps.Driver
        AND TIME > '0:00.000' -- Prevent rows with null values from being returned. (needed according to Tzvika)
        GROUP BY drivers.Nationality) AS t2 
        ON t1.Nationality = t2.Nationality -- Use the nationality as the key for joining
LEFT JOIN 
        (SELECT -- Get the latest date each nationality of drivers won a race
            drivers.Nationality, 
            MAX(winners.Date) AS latest
        FROM winners, drivers
        WHERE drivers.Driver = winners.Winner
        GROUP BY drivers.Nationality) AS t3 
        ON t1.Nationality = t3.Nationality -- Use the nationality as the key for joining
HAVING min_time IS NOT NULL AND latest IS NOT NULL -- Remove the rows that has NULL values. (needed according to Tzvika) 
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))