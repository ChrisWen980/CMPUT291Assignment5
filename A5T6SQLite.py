'''
CMPUT 291
Winter 2021
Ahmad Amin 1623338
Chris  Wen 1619368
'''

import sqlite3
import time

def main():
    print('Task 6: Increase the rental cost/night by 10% for all properties in a neighbourhood given at run-time (e.g., using command line prompt or via an application parameter)')
    print("Type in the desired neighbourhood to change values for: ")
    # Take the input
    inpt = input()

    # Setup
    conn = sqlite3.connect('A5.db')
    c = conn.cursor()

    # Query for neighbourhood
    c.execute("SELECT COUNT(1) From Listings L WHERE L.neighbourhood = ?;", (inpt,))

    # Check if the neighbourhood exists
    if not c.fetchone()[0]:
        # Print error message
        print("Neighbourhood does not exist, task has been vacuosly completed.")
        return

    # Query for price and neighbourhood before update
    c.execute("SELECT price, neighbourhood From Listings WHERE neighbourhood = ?;", (inpt,))

    # Print price and neighbourhood before update
    rows=c.fetchall()
    print("These are the prices before update: ")
    print("Format: price, neighbourhood")
    for row in rows:
        print(row[0], "  ", row[1])

    # Run query
    startTime = time.time()
    c.execute("UPDATE Listings SET price=round(price*1.1, 6) WHERE neighbourhood = ?;", (inpt,))
    endTime = time.time()

    # Print price and neighbourhood after update
    c.execute("SELECT price, neighbourhood From Listings WHERE neighbourhood = ?;", (inpt,))
    rows=c.fetchall()
    print("These are the prices after update: ")
    print("Format: price, neighbourhood")
    for row in rows:
        print(row[0], "  ", row[1])

    # Print running time
    print("Time taken to execute query: {} ms".format((endTime - startTime)*10**3))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()

    


