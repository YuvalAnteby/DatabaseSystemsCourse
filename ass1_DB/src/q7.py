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
    # Return drivers who won with Alfa Romeo or drivers who have a Japanese (JPN) nationality.
    # Sort the results alphabetically. Do not return duplicates. Return a table with one column “driver”.`
    cursor.execute("""
(SELECT winners.Winner as 'driver' -- Get the drivers of Alfa Romeo
FROM winners
WHERE winners.Car='Alfa Romeo')
UNION -- We want both so we use the union function
(SELECT drivers.Driver as 'driver' -- Get the drivers from Japan
FROM drivers
WHERE drivers.Nationality='JPN')
ORDER BY driver ASC
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))