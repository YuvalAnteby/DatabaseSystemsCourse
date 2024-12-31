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
CREATE TABLE ratings(
    rating_ID INT PRIMARY KEY AUTO_INCREMENT,
    rating INT,
    patient INT,
    doctor INT,
    FOREIGN KEY (patient) REFERENCES patients(patient_ID),
    FOREIGN KEY (doctor) REFERENCES doctors(doctor_ID));
    """
    cursor.execute(query)
    mydb.commit()
    cursor.close()
    mydb.close()