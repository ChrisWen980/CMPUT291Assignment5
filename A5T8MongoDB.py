from pymongo import MongoClient
import time

def main():    
    print('Task 8: Given a listing_id at run-time (e.g., using command line prompt or via an application parameter) find the host_name, rental_price and the most recent review for that listing.')
    print("Type in the desired listing_id: ")
    desiredListing = input()

    mongo_client = MongoClient()
    mongoDB = mongo_client['A5db']
    listingCol = mongoDB['listingCol']


    startTime = time.time()
    reslt = mongoDB.listingCol.aggregate([{"$unwind": "$reviews"}, {"$match": {"reviews.listing_id": desiredListing}}, {"$group": {"_id": "$id", "host_name": {"$first": "$host_name"}, "price": {"$first": "$price"}, "comments": {"$first": "$reviews.comments"}}}])
    print("(host_name, price, reviews.comments)")
    for row in reslt:
        print(row["host_name"], row["price"], row["reviews.comments"], sep=", ")
    endTime = time.time()



    print("Time taken to execute query: {} ms".format((endTime - startTime)*10**3))

if __name__ == "__main__":
    main()