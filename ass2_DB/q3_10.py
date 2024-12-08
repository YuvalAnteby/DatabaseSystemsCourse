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
    query = """
INSERT INTO order_customer(order_id, customer_id) 
VALUES
     (1, '123456789'), 
     (2, '987654321'), 
     (3, '112233445'), 
     (4, '223344556'),
     (5, '334455667'), 
     (6, '445566778'), 
     (7, '556677889'), 
     (8, '667788990'),
     (9, '778899001'), 
     (10, '889900112')
    """
    cursor.execute(query)
    mydb.commit()
    cursor.close()
    mydb.close()