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
    # To ensure their inventory is well-stocked, the operations team needs to know how many size
    # options are available for each shoe. This will help them identify shoes with limited size
    # options and adjust their stock accordingly.
    # Write a query to list all shoe names with the count of sizes available
    # for each including shoes that don’t have any size.
    query = """
SELECT s.shoe_name, COUNT(ss.size_id) AS shoe_count
FROM shoe AS s
-- Joining the tables on the matching keys between the sizes and shoes
JOIN shoe_size AS ss
    ON s.shoe_id = ss.shoe_id
JOIN size AS sz
    ON ss.size_id = sz.size_id
-- Showing for each shoe name
GROUP BY s.shoe_name
-- Order from lowest to highest (not requested only for ease of use)
ORDER BY s.shoe_name
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))
