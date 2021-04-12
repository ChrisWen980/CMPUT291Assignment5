'''
CMPUT 291
Winter 2021
Ahmad 1623338
'''
import sqlite3
import time

def main():
    print("Task 4: Find which listed property(ies) has(have) not received any review, order them by listing_id and output the top 10")

    conn = sqlite3.connect('A5.db')
    c = conn.cursor()

    startTime = time.time()
    c.execute("SELECT L.name, L.id FROM Listings L WHERE NOT EXISTS (SELECT * From Reviews R WHERE L.id = R.listing_id) ORDER BY L.id ASC LIMIT 10;")
    endTime = time.time()
    
    rows=c.fetchall()

    print("(name, id)")
    for row in rows:
        print(row)

    print("Time taken to execute query: {} ms".format((endTime - startTime)*10**3))

    conn.close()

if __name__ == "__main__":
    main()


