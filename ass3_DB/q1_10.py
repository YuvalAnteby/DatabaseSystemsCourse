import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yuval2001",
        database="Hosppdd",
        port='3307',
    )
    cursor = mydb.cursor()
    #
    query = """
CREATE TABLE opinions(
    rating INT PRIMARY KEY,
    opinion VARCHAR(255),
    FOREIGN KEY (rating) REFERENCES ratings(rating_ID));
    """
    cursor.execute(query)
    mydb.commit()
    cursor.close()
    mydb.close()