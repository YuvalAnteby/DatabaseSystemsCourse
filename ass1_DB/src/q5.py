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
    # Write a query to find the average amount of points for each car, for cars whose fastest lap time was less
    # than 2 minutes. Order the average points in descending order.
    # The answer should contain both the car and the average points as “avg_pts”.
    query = """

    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))