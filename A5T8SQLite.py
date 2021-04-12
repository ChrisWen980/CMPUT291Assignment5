'''
CMPUT 291
Winter 2021
Ahmad 1623338
'''
import sqlite3
import time

def main():
    print('Task 8: Given a listing_id at run-time (e.g., using command line prompt or via an application parameter) find the host_name, rental_price and the most recent review for that listing.')

    conn = sqlite3.connect('A5.db')
    c = conn.cursor()

    print("Type in the desired listing_id: ")
    inpt = input()
    c.execute("SELECT COUNT(1) From Reviews R WHERE R.listing_id = ?;", (inpt,))
    if not c.fetchone()[0]:
        print("Neighbourhood does not exist, task has been vacuosly completed.")
        return

    print("(host_name, price, date of recent review, review)")

    startTime = time.time()
    c.execute("SELECT L.host_name, L.price, MAX(R.date), R.comments FROM Reviews R, Listings L WHERE R.listing_id = ? AND R.listing_id = L.id GROUP BY R.listing_id ;", (inpt,))
    endTime = time.time()

    print(c.fetchone())

    print("Time taken to execute query: {} ms".format((endTime - startTime)*10**3))

    conn.close()

if __name__ == "__main__":
    main()

    


