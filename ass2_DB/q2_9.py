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
    # order shoe : (order id : INT, shoe id : INT)
    # Foreign Keys:
    # order shoe(order id) → company order(order id)
    # order shoe(shoe id) → shoe(shoe id)
    query = """
CREATE TABLE order_shoe(
order_id INT REFERENCES company_order(order_id),
shoe_id INT REFERENCES shoe(shoe_id),
PRIMARY KEY(order_id, shoe_id));
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))