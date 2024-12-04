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
    # The company has started offering pre-orders for special edition sneakers.
    # Write a query that add a pre_order_available column to the upcoming table
    # to indicate whether pre-orders are enabled, making it a single-bit type and
    # default value 0.
    query = """
ALTER TABLE upcoming 
ADD pre_order_available BIGINT DEFAULT 0;
    """
    cursor.execute(query)
    mydb.commit()
    cursor.close()
    mydb.close()