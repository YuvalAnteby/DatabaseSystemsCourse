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
    # Write a query that returns a list of locations(location) included in the table where in some day,
    # there were more new deaths(new_deaths) than new cases(new_cases).
    # The result should only include the location names, without duplicates.

    query = """
-- Selecting only distinct locations in order to print only locations and once per location. 
SELECT  DISTINCT location
FROM    covid_deaths
-- Checking for new deaths that are greater than new cases in a date.
WHERE   new_deaths > new_cases;
    """
    cursor.execute(query)
    print('\n'.join(str(row) for row in cursor.fetchall()))
