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
    #size : (size id : INT, european number : TINY INT NOT NULL, us number :TINY INT)
    query = """
CREATE TABLE size(
size_id INT,
european_number TINYINT NOT NULL,
us_number TINYINT, 
PRIMARY KEY(size_id));
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))