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
    # Connection table of shoes and orders:
    # order customer : (order id : INT, customer id : INT)
    # Foreign Keys:
    # order customer(order id) → company order(order id)
    # order customer(customer id) → customer(customer id)
    query = """
CREATE TABLE order_customer(
order_id INT REFERENCES company_order(order_id),
customer_id INT REFERENCES customer(customer_id),
PRIMARY KEY(order_id, customer_id));
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))