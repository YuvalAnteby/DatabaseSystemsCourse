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
    # Customers details:
    # customer : (customer id : VARCHAR(15) CHECK LENGTH
    # EXACTLY 9, first name : VARCHAR(31) NOT NULL, last name :
    # VARCHAR(31) NOT NULL, email : VARCHAR(255) UNIQUE
    # NOT NULL, city id : INT NOT NULL)
    query = """
CREATE TABLE customer(
customer_id VARCHAR(15) CHECK (LENGTH(customer_id) = 9),
first_name VARCHAR(31) NOT NULL,
last_name VARCHAR(31) NOT NULL,
email VARCHAR(255) UNICODE NOT NULL,
city_id INT NOT NULL REFERENCES city(city_id),
PRIMARY KEY(customer_id));
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))