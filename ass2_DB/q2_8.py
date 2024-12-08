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
    # All of the company orders:
    # company order : (order id : INT
    # order date : DAT ET IME NOT NULL)
    query = """
CREATE TABLE company_order(
order_id INT,
order_date DATETIME NOT NULL,
PRIMARY KEY(order_id));
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))