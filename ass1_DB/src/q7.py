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
        (SELECT     winners.Winner as 'driver'
        FROM        winners
        WHERE       winners.Car='Alfa Romeo')
        UNION
        (SELECT     drivers.Driver as 'driver'
        FROM        drivers
        WHERE       drivers.Nationality='JPN')
        ORDER BY    driver ASC
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))