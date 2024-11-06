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
    query = """
            SELECT date, new_cases, continent
            FROM covid_deaths
            WHERE continent = "South America" AND new_cases > 150000
            ORDER BY new_cases ASC
    """
    cursor.execute(query)
    print('\n'.join(str(row) for row in cursor.fetchall()))
