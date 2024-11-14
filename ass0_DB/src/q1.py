import mysql.connector
if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="covid_db",
        port='3307',
    )
    cursor = mydb.cursor()
    # Write a query that returns a list of all locations included in the table(location).
    # The result should only contain the location names, without duplicates.

    query = """
-- Get the locations using DISTINCT in order to not get duplicates.
SELECT  DISTINCT location
FROM    covid_deaths;
            """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))