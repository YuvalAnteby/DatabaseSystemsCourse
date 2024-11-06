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
    # Selecting only israel as location and using DESC in order to get the higher cases' dates first
    # Using limit 20 to get only the top 20 dates
    query = """
            SELECT date, new_cases
            FROM covid_deaths
            WHERE location = "Israel"
            ORDER BY new_cases DESC
            LIMIT 20
    """
    cursor.execute(query)
    print('\n'.join(str(row) for row in cursor.fetchall()))
