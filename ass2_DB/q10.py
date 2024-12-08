import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yuval2001",
        database="biu_shoes",
        port='3307',
    )
    cursor = mydb.cursor()
    # The marketing team is planning a major campaign that combines regular inventory with upcoming
    # special releases. They need a consolidated list of all available shoe names and upcoming
    # collections to design their promotional materials.
    # Write a query to combine the list of shoe names from the inventory with the list of special
    # upcoming release event names under namecolumn, and include an additional column, source,
    # indicating whether the entry is from the 'Inventory' or an 'Upcoming Release'.
    # (Tip: we can hard coded a value as a column using aliasing)
    query = """
-- Get the shoe's names from the shoe table as the ones in the inventory
SELECT shoe.shoe_name AS namecolumn, 
       'Inventory' AS source
FROM shoe
-- Use union for getting both into the same column
UNION ALL
-- Get the shoe's names from the upcoming table as the ones in the upcoming release
SELECT upcoming.collection_name AS namecolumn, 
       'Upcoming Release' AS source
from upcoming
-- Order from lowest to highest (not requested only for ease of use)
ORDER BY namecolumn
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))
