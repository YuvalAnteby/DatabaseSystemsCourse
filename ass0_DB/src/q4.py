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
    # Find the top 20 days in terms of new covid cases in Israel(date, new_cases). In the result, include the
    # date and the amount of new cases. The result should be ordered so that days with more cases are higher.
    query = """
SELECT date, new_cases
FROM        covid_deaths
-- Selecting only israel as location
WHERE       location = "Israel"
-- Using DESC in order to get the higher cases dates first
ORDER BY    new_cases DESC
-- Using limit 20 to get only the top 20 dates
LIMIT       20;
    """
    cursor.execute(query)
    print('\n'.join(str(row) for row in cursor.fetchall()))
