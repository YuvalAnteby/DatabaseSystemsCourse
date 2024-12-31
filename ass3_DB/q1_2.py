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
CREATE TABLE patients(
    patient_ID INT PRIMARY KEY,
    name VARCHAR(255),
    height INT,
    weight INT,
    gender BIT);
    """
    cursor.execute(query)
    mydb.commit()
    cursor.close()
    mydb.close()