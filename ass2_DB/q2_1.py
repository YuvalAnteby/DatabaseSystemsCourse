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
    # Using the requirements provided by our architecture team. Write proper queries (10) to create the
    # following tables in the database. Ensure you select the appropriate data types and constraints.
    # Stores shoe details:
    # shoe : (shoe id : INT, shoe name : VARCHAR(31) NOT NULL, price : SMALLINT NOT NULL)
    query = """
CREATE TABLE shoe(
shoe_id INT,
shoe_name VARCHAR(31) NOT NULL,
price SMALLINT NOT NULL,
PRIMARY KEY(shoe_id));
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))