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
CREATE TABLE hospitals(
    hospital_ID INT PRIMARY KEY,
    name VARCHAR(255));
    """
    cursor.execute(query)
    mydb.commit()
    cursor.close()
    mydb.close()