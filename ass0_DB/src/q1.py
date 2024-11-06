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
    # Get the locations using DISTINCT in order to not get duplicates.
    query = """
            SELECT DISTINCT location
            FROM covid_deaths
            """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))