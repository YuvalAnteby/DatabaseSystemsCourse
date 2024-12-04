import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yuval2001",
        database="biu_shoes",
        port='3307',
    )
    cursor = mydb.cursor()
    # The company wants to populate the uk number column in the size table
    # based on the above size chart.
    # Write SQL queries (5) to update the uk number column values.
    # European Size = 39, US Size = 7, UK Size = 6
    query = """
UPDATE size
SET uk_number = 6
WHERE european_number = 39 
AND us_number = 7;
    """
    cursor.execute(query)
    mydb.commit()
    cursor.close()
    mydb.close()