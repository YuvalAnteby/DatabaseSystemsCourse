import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yuval2001",
        port='3307',
    )
    cursor = mydb.cursor()
    # Create the schema for the DB
    query = """
CREATE DATABASE `Hosppdd`;
    """
    cursor.execute(query)