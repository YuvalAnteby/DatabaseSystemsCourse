import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="f1_data",
        port='3307',
    )
    cursor = mydb.cursor()
    # How many drivers start with the letter A? Return one numerical cell with the result
    query = """
-- Using COUNT for counting the names, using DISTINCT for getting each name only once. 
SELECT COUNT(DISTINCT Driver) as Driver_Count
FROM drivers
-- Using LIKE to get all the names starting with 'A' or 'a'
WHERE drivers.Driver LIKE "A%" OR drivers.Driver LIKE "a%";
         """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))
