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
CREATE TABLE doctors(
    doctor_ID INT,
    hospital INT,
    name VARCHAR(255),
    consultant INT,
    PRIMARY KEY (doctor_ID, hospital),
    FOREIGN KEY (consultant) REFERENCES doctors(doctor_ID),
    FOREIGN KEY (hospital) REFERENCES hospitals(hospital_ID));
    """
    cursor.execute(query)
    mydb.commit()
    cursor.close()
    mydb.close()