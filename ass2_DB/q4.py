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
    # The company has decided to expand to the UK market.
    # Write a query that alter the size table to add the uk number TINY INT
    # column and update the values accordingly.
    query = """
ALTER TABLE shoe_size
ADD uk_number TINYINT;
    """
    cursor.execute(query)
    mydb.commit()
    cursor.close()
    mydb.close()