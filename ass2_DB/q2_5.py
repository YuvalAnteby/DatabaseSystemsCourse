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
    # Countries information:
    # country : (country id : INT, country name : VARCHAR(63) NOT NULL)
    query = """
CREATE TABLE country(
country_id INT,
country_name VARCHAR(63) NOT NULL,
PRIMARY KEY(country_id)
);
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))