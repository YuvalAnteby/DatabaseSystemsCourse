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
    query = """
CREATE TABLE treats(
    patient INT,
    doctor INT,
    hospital INT,
    PRIMARY KEY (patient, doctor, hospital),
    FOREIGN KEY (patient) REFERENCES patients(patient_ID),
    FOREIGN KEY (doctor) REFERENCES doctors(doctor_ID),
    FOREIGN KEY (hospital) REFERENCES hospitals(hospital_ID));
    """
    cursor.execute(query)
    mydb.commit()
    cursor.close()
    mydb.close()