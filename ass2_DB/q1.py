import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yuval2001",
        port='3307',
    )
    cursor = mydb.cursor()
    # Create a database for BIU Shoes with the name: biu shoes Write a query that does so.
    query = """
CREATE DATABASE `biu_shoes`
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))