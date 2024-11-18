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
    # What is the total amount of wins in 2001, for the team who had the most wins in 2000?
    # Return a single numerical cell.
    query = """
SELECT 	COUNT(Car) -- Regard a team as a car value.
FROM 	winners
WHERE 	Year(winners.Date) = 2001 -- Needed year.
		AND winners.Car = ( -- Get the one with the most wins in 2000.
			SELECT Car
			FROM 		winners
			WHERE 		Year(winners.Date) = 2000
            GROUP BY 	Car
            ORDER BY 	COUNT(*) DESC
            LIMIT 		1
            );
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))