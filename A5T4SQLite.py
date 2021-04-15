'''
CMPUT 291
Winter 2021
Ahmad Amin 1623338
Chris  Wen 1619368
'''

import sqlite3
import time

def main():
    print("Task 4: Find which listed property(ies) has(have) not received any review, order them by listing_id and output the top 10")

    # Setup
    conn = sqlite3.connect('A5.db')
    c = conn.cursor()

    # Run the query
    startTime = time.time()
    c.execute("SELECT L.name, L.id FROM Listings L WHERE NOT EXISTS (SELECT * From Reviews R WHERE L.id = R.listing_id) ORDER BY L.id ASC LIMIT 10;")
    endTime = time.time()
    
    # Print the result
    rows=c.fetchall()
    print("Format: name, id")
    for row in rows:
        print(row[0], row[1])

    # Print the running time
    print("Time taken to execute query: {} ms".format((endTime - startTime)*10**3))

    conn.close()

if __name__ == "__main__":
    main()


