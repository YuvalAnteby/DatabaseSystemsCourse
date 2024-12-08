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
    # The finance team wants a high-level summary of sales for each shoe to evaluate product performance.
    # They need a summary that shows the total revenue generated by each shoe, across all orders.
    # Write a query to create a view (total sales per shoe) summarizing total sales per shoe,
    # including the shoe ID, name, and total revenue.
    # Write another query to display the entire view data.
    query = """
-- Show the total sales using the view from q11_1.py
SELECT * 
FROM total_sales_per_shoe;
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))