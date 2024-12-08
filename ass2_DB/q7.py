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
    # The marketing team at BIU Shoes is curious about which customers generate
    # the most revenue for the company. They want a clear breakdown of the total
    # revenue each customer has contributed, based on their purchases.
    # Write a query to calculate the total revenue generated by each customer,
    # returning their first name, last name, and total amount spent if at all.
    query = """
-- Selecting the first+last names and the sum of shoe prices the customer bought 
SELECT c.first_name, 
       c.last_name,
       SUM(s.price) AS total_revenue
FROM customer AS c
-- Joining the tables on the matching keys between the customers and shoes bought
JOIN order_customer AS oc 
    ON c.customer_id = oc.customer_id
JOIN order_shoe AS os
    ON oc.order_id = os.order_id
JOIN shoe AS s
    ON os.shoe_id = s.shoe_id
-- Grouping by the id of the customer to have the sum for each customer
GROUP BY c.customer_id
-- Order by for ease of use, no need according to the assigment
ORDER BY total_revenue DESC
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))
