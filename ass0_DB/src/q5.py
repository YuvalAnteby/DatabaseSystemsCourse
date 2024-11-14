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
    # Write a query to find the dates(date), locations(location) and number of new cases(new_cases), where the number
    # of new cases was equal to the number of  weekly hospital admissions(weekly_hosp_admissions).
    # This number cannot be 0. The higher the number, the higher the result in the order.
    query = """
SELECT      date, location, new_cases, weekly_hosp_admissions
FROM        covid_deaths
WHERE       new_cases = weekly_hosp_admissions AND NOT new_cases = 0
ORDER BY    new_cases DESC;
    """
    cursor.execute(query)
    print('\n'.join(str(row) for row in cursor.fetchall()))