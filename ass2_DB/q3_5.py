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
    query = """
INSERT INTO country(country_id, country_name) 
VALUES
     (1, 'Israel'), 
     (2, 'Canada'), 
     (3, 'United States'), 
     (4, 'Germany'), 
     (5, 'France'), 
     (6, 'Japan'), 
     (7, 'Australia'), 
     (8, 'Italy'), 
     (9, 'Spain'), 
     (10, 'Brazil')
    """
    cursor.execute(query)
    mydb.commit()
    cursor.close()
    mydb.close()