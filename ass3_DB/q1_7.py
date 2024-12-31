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
CREATE TABLE registery(
    registry_ID INT PRIMARY KEY AUTO_INCREMENT,
    patient INT,
    hospital INT,
    prev_disease INT,
    new_disease INT NOT NULL,
    FOREIGN KEY (patient) REFERENCES patients(patient_ID),
    FOREIGN KEY (hospital) REFERENCES hospitals(hospital_ID),
    FOREIGN KEY (prev_disease) REFERENCES diseases(disease_ID),
    FOREIGN KEY (new_disease) REFERENCES diseases(disease_ID));
    """
    cursor.execute(query)
    mydb.commit()
    cursor.close()
    mydb.close()