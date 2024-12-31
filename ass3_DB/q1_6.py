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
CREATE TABLE diseases(
    disease_ID INT PRIMARY KEY,
    name VARCHAR(255),
    severity VARCHAR (255),
    cure INT,
    FOREIGN KEY (cure) REFERENCES medicines(medicine_ID));
    """
    cursor.execute(query)
    mydb.commit()
    cursor.close()
    mydb.close()