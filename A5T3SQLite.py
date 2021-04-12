'''
CMPUT 291
Winter 2021
Ahmad 1623338
'''
import sqlite3
import time

def main():
    print("Task 3: Find how many listings each host own, ordering the output by host_id and only output the top 10")

    conn = sqlite3.connect('A5.db')
    c = conn.cursor()

    startTime = time.time()
    c.execute("SELECT host_id, count(*) FROM Listings GROUP BY host_id ORDER BY host_id ASC LIMIT 10")
    endTime = time.time()
    
    rows=c.fetchall()

    print("(host_id, numListings)")
    for row in rows:
        print(row)
    

    print("Time taken to execute query: {} ms".format((endTime - startTime)*10**3))

    conn.close()

if __name__ == "__main__":
    main()


