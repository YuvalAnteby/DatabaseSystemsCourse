import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="biu_shoes",
        port='3307',
    )
    cursor = mydb.cursor()
    # The company wants to populate the uk number column in the size table
    # based on the above size chart.
    # Write SQL queries (5) to update the uk number column values.
    # European Size = 38, US Size = 6, UK Size = 5
    query = """
UPDATE size
SET uk_number = 5
WHERE european_number = 38
AND us_number = 6;
    """
    cursor.execute(query)
    mydb.commit()
    cursor.close()
    mydb.close()