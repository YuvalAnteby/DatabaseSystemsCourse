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
    query = """

    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))