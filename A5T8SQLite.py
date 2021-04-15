'''
CMPUT 291
Winter 2021
Ahmad Amin 1623338
Chris  Wen 1619368
'''

import sqlite3
import time

def main():
    print('Task 8: Given a listing_id at run-time (e.g., using command line prompt or via an application parameter) find the host_name, rental_price and the most recent review for that listing.')

    # Setup
    conn = sqlite3.connect('A5.db')
    c = conn.cursor()

    print("Type in the desired listing_id: ")
    # Take in input
    inpt = input()
    
    # Query to check if listing_id exists
    c.execute("SELECT COUNT(1) From Reviews R WHERE R.listing_id = ?;", (inpt,))
    
    # Check if listing_id exists
    if not c.fetchone()[0]:
        # Print error message
        print("Neighbourhood does not exist, task has been vacuosly completed.")
        return

    # Run query
    startTime = time.time()
    c.execute("SELECT L.host_name, L.price, MAX(R.date), R.comments FROM Reviews R, Listings L WHERE R.listing_id = ? AND R.listing_id = L.id GROUP BY R.listing_id ;", (inpt,))
    endTime = time.time()

    # Print result
    rows = c.fetchall()
    print("Format: host_name, price, date of recent review, review")
    for row in rows:
        print(row[0], row[1], row[2], row[3])

    # Print running time
    print("Time taken to execute query: {} ms".format((endTime - startTime)*10**3))

    conn.close()

if __name__ == "__main__":
    main()

    


