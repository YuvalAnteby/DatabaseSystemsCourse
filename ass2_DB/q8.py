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
    # The product team wants to better understand the price distribution of shoes for different sizes.
    # This analysis will help them determine if certain sizes have higher-priced shoes.
    # Write a query to find the average price of shoes available in each size,
    # returning the European and US sizes among with the average, and order them from highest to lowest.
    query = """
SELECT european_number, us_number, AVG(s.price) AS average_price
FROM size AS sz
-- Joining the tables on the matching keys between the sizes and shoes
JOIN shoe_size AS ss
    ON sz.size_id = ss.size_id
JOIN shoe AS s
    ON ss.shoe_id = s.shoe_id
-- Showing for each shoe size
GROUP BY sz.size_id
-- Order from highest to lowest
ORDER BY average_price DESC
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))
