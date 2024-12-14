import mysql.connector

if __name__ == '__main__':
    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="biu_shoes",
        port="3307",
    )
    
    cursor = mydb.cursor()

    # Select the shoe name from the 'shoe' table
    # The 'shoe' table is aliased as 's'
    # Perform a LEFT JOIN with the 'order_shoe' table (aliased as 'os')
    # Join the tables where shoe_id matches in both tables
    # Filter out the shoes that have not been ordered (no matching shoe_id in 'order_shoe')
    # Display unsold shoes.
    query = """
    SELECT s.shoe_name
    FROM shoe AS s
    LEFT JOIN order_shoe AS os
    ON s.shoe_id = os.shoe_id
    WHERE os.shoe_id IS NULL;
    """
    cursor.execute(query)
    print(', '.join(str(row[0]) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()
