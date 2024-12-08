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
    # Cities information:
    # city : (city id : INT, city name : VARCHAR(63) NOT NULL, country id :
    # INT NOT NULL)
    # Foreign Keys:
    # city(country id) → country(country id)
    query = """
CREATE TABLE city(
city_id INT,
city_name VARCHAR(63) NOT NULL,
country_id INT NOT NULL REFERENCES country(country_id),
PRIMARY KEY(city_id));
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))