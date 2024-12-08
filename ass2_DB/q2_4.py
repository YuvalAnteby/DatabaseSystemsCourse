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
    # Special edition upcoming sneakers releases:
    # upcoming : (special id : INT, shoe id : INT NOT NULL, collection name :
    # VARCHAR(31), release date : DATETIME)
    # Foreign Keys:
    # upcoming(shoe id) → shoe(shoe id)
    query = """
CREATE TABLE upcoming(
special_id INT REFERENCES shoe(shoe_id),
shoe_id INT NOT NULL,
collection_name VARCHAR(31),
release_date DATETIME,
PRIMARY KEY(special_id));
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))