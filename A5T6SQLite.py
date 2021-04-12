'''
CMPUT 291
Winter 2021
Ahmad 1623338
'''
import sqlite3
import time

def main():
    print('Task 6: Increase the rental cost/night by 10% for all properties in a neighbourhood given at run-time (e.g., using command line prompt or via an application parameter)')
    print("Type in the desired neighbourhood to change values for: ")
    inpt = input()

    conn = sqlite3.connect('A5.db')
    c = conn.cursor()

    c.execute("SELECT COUNT(1) From Listings L WHERE L.neighbourhood = ?;", (inpt,))

    if not c.fetchone()[0]:
        print("Neighbourhood does not exist, task has been vacuosly completed.")
        return

    startTime = time.time()
    c.execute("UPDATE Listings SET price=round(price*1.1, 6) WHERE neighbourhood = ?;", (inpt,))
    endTime = time.time()

    print("Time taken to execute query: {} ms".format((endTime - startTime)*10**3))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()

    


