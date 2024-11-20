import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yuval2001",
        database="f1_data",
        port='3307',
    )
    cursor = mydb.cursor()
    # Find all pairs of Grand Prix tournaments that have the exact same amount of laps, and that this amount
    # is greater than 100. Do not return duplicates. Return the following columns: GP1, GP2, Laps.
    # Make sure that GP1 is alphabetically before GP2 (for example, <Apple, Banana> and not <Banana, Apple>).
    query = """
SELECT DISTINCT w1.`Grand Prix` AS gp1, w2.`Grand Prix` AS gp2, w1.Laps
FROM 			winners AS w1, winners AS w2
WHERE 			w1.Laps = w2.Laps
AND 			w1.Laps > 100
AND 			w1.`Grand Prix` < w2.`Grand Prix`
    """
    cursor.execute(query)
    print(', '.join(str(row) for row in cursor.fetchall()))