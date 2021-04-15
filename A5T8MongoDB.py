'''
CMPUT 291
Winter 2021
Ahmad Amin 1623338
Chris  Wen 1619368
'''

from pymongo import MongoClient
import time

def main():    
    print('Task 8: Given a listing_id at run-time (e.g., using command line prompt or via an application parameter) find the host_name, rental_price and the most recent review for that listing.')
    print("Type in the desired listing_id: ")
    # Take in input
    desiredListing = int(input())

    # Setup
    mongo_client = MongoClient()
    mongoDB = mongo_client['A5db']
    listingCol = mongoDB['listingCol']

    # Query to check if the listing_id exists
    check = mongoDB.listingCol.find({"reviews.listing_id": desiredListing})

    # Check if listing_id exists
    if check.count() != 0:
        # Run query
        startTime = time.time()
        aggResult = mongoDB.listingCol.aggregate([{"$unwind": "$reviews"}, {"$match": {"reviews.listing_id": desiredListing}}, {"$group": {"_id": "$id", "host_name": {"$first": "$host_name"}, "price": {"$first": "$price"}, "date": {"$last": "$reviews.date"}, "comments": {"$last": "$reviews.comments"}}}])
        endTime = time.time()

        # Print results
        print("Format: host_name, price, date, comments")
        for row in aggResult:
            print(row["host_name"], row["price"], row["date"], row["comments"], sep=", ")

        # Print running time
        print("Time taken to execute query: {} ms".format((endTime - startTime)*10**3))
    
    else:
        # Print error message
        print("This neighbourhood does not exist")

if __name__ == "__main__":
    main()