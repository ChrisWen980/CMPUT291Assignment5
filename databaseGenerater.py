'''
CMPUT 291 Winter 2021
Ahmad 1623338

Make sure you run the code from the directory that contains YVR_Airbnb_reviews.csv, YVR_Airbnb_listings_summary.csv, and databaseGnerater.py.
'''

import csv
import sqlite3
from collections import namedtuple

csv_reviews = "YVR_Airbnb_reviews.csv"
csv_listings = "YVR_Airbnb_listings_summary.csv"
listing = namedtuple("listing", "id, name, host_id, host_name, neighbourhood, room_type, price, minimum_nights, availability_365")
review = namedtuple("review", "listing_id, id, date, reviewer_id, reviewer_name, comments")

def main():
    '''
    Makes a database A5.db and from csv_reivews and csv_listings, creates and populates appropriate tables.
    '''
    conn = sqlite3.connect('A5.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Listings (id integer PRIMARY KEY, name text, host_id integer, host_name text, neighbourhood text, room_type text, price integer, minimum_nights integer, availability_365 integer);")
    c.execute("CREATE TABLE IF NOT EXISTS Reviews (id integer PRIMARY KEY, listing_id integer, date text, reviewer_id integer, reviewer_name text, comments text);")

    ################ Making table: Listings    
    with open(csv_listings, newline ='', encoding = 'utf-8') as file:
        for summary in map(listing._make, csv.reader(file)):
            try:
                id = int(summary.id)
                name = str(summary.name)
                host_id = int(summary.host_id)
                host_name = str(summary.host_name)
                neighbourhood = str(summary.neighbourhood)
                room_type = str(summary.room_type)
                price = int(summary.price)
                minimum_nights = int(summary.minimum_nights)
                availability_365 = int(summary.availability_365)
            except:
                continue

            try:
                c.execute("INSERT INTO Listings VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", (id, name, host_id, host_name, neighbourhood, room_type, price, minimum_nights, availability_365))
            except sqlite3.IntegrityError:
                print("Value you are trying to add is already in database, maybe the database is already filled?")
                return

    ################ Making table: Reviews    
    with open(csv_reviews, newline ='', encoding = 'utf-8') as file:
        for rvw in map(review._make, csv.reader(file)):
            try:
                listing_id = int(rvw.listing_id)
                id = int(rvw.id)
                date = str(rvw.date)
                reviewer_id = int(rvw.reviewer_id)
                reviewer_name = str(rvw.reviewer_name)
                comments = str(rvw.comments)
            except:
                continue
            c.execute("INSERT INTO Reviews VALUES (?, ?, ?, ?, ?, ?);", (id, listing_id, date, reviewer_id, reviewer_name, comments))

    conn.commit()
    conn.close()
    print("Database filled")

def check():
    '''
    Shows output from table Listings and expected output from table Listings.
    Shows output from table Reviews and expected output from table Reviews.
    '''
    print("Checking if Listings table has correct values.")
    conn = sqlite3.connect('A5.db')
    c = conn.cursor()
    c.execute("SELECT MIN(host_id), MAX(host_id), AVG(host_id), COUNT(host_id) FROM listings;")
    print(c.fetchall())
    print("Should look like")
    print("6033, 387534175, 115176061.858295, 4340")
    print("Checking if Reviews table has correct values.")
    c.execute("SELECT MIN(id), MAX(id), AVG(id), COUNT(id) FROM reviews;")
    print(c.fetchall())
    print("Should look like")
    print("26444, 730124064, 370354766.849158, 147936")
    conn.close()

if __name__ == "__main__":
    main()
    check()
            
        
