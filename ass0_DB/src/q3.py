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
    # Selecting only distinct locations in order to print only locations and once per location.
    # checking for new deaths that are greater than new cases in a date.
    query = """
            SELECT DISTINCT location
            FROM covid_deaths
            WHERE new_deaths > new_cases
    """
    cursor.execute(query)
    print('\n'.join(str(row) for row in cursor.fetchall()))
