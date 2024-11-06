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
            SELECT date, location, new_cases, weekly_hosp_admissions
            FROM covid_deaths
            WHERE new_cases = weekly_hosp_admissions AND NOT new_cases = 0
            ORDER BY new_cases DESC
    """
    cursor.execute(query)
    print('\n'.join(str(row) for row in cursor.fetchall()))