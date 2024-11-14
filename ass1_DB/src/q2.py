import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yuval2001",
        database="f1_data",
        port='3307',
    )
    cursor = mydb.cursor()
    # How many drivers end with the letter N? Return one numerical cell with the result
    query = """
-- Using COUNT for counting the names, using DISTINCT for getting each name only once. 
SELECT  COUNT(DISTINCT Driver) as Driver_Count
FROM    drivers
-- Using LIKE to get all the names ending with 'N' or 'n'
WHERE   drivers.Driver LIKE "%N" OR drivers.Driver LIKE "%n";
         """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))
