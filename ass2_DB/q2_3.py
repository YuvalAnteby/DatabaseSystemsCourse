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
    # shoe size : (shoe id : INT, size id : INT)
    # Foreign Keys:
    # shoe size(shoe id) → shoe(shoe id)
    # shoe size(size id) → size(size id)
    query = """
CREATE TABLE shoe_size(
shoe_id INT REFERENCES shoe(shoe_id),
size_id INT REFERENCES size(size_id),
PRIMARY KEY(shoe_id, size_id)); 
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))