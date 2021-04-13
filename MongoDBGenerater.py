import csv
import sqlite3
from pymongo import MongoClient
from collections import namedtuple

def main():
    '''
    Makes a database A5.db and from csv_reivews and csv_listings, creates and populates appropriate tables.
    '''
    conn = sqlite3.connect('A5.db')
    c = conn.cursor()

    mongo_client = MongoClient()
    mongoDB = mongo_client['A5db']

    c.execute("SELECT * FROM Listings ORDER BY id ASC;")
    listingData = c.fetchall()
    c.execute("SELECT * FROM Reviews ORDER BY listing_id ASC;")
    reviewsData = c.fetchall()

    print("This is listings length: ", len(listingData), "\n")
    print("This is reviews length: ", len(reviewsData), "\n")


    try:
        listingCol = mongo_client.mongoDB.create_collection('listingCol')
    except:
        listingCol = mongoDB['listingCol']
        listingCol.drop()

    reviewsList = []
    print(len(reviewsData), "\n")

    for i in range(len(listingData)):
        for j in range(len(reviewsData)):
            if reviewsData[j][1] == listingData[i][0]:
                reviewsList.append({"id": reviewsData[j][0], "date": reviewsData[j][2], "reviewer_id": reviewsData[j][3], "reviewer_name": reviewsData[j][4], "comments": reviewsData[j][5]})
            
        insertionDict = { "id": listingData[i][0], "name": listingData[i][1], "host_id": listingData[i][2], "host_name": listingData[i][3], "neighbourhood": listingData[i][4], "room_type": listingData[i][5], "price": listingData[i][6], "minimum_nights": listingData[i][7], "availability_365": listingData[i][8], "reviews": reviewsList}
        listingCol.insert_one(insertionDict)
        del reviewsList[:]

    conn.commit()
    conn.close()
    print("Database filled\n")

    print("Checking if mongoDB has correct values.\n")
    print("Should look like: \n")
    print('{ "_id" : null, "min" : 6033, "max" : 387534175, "avg" : 115176061.85829493, "count" : 4340 } \n')
    aggResult = mongoDB.listingCol.aggregate([{"$group": {"_id": "null", "min": {"$min": "$host_id"}, "max": {"$max": "$host_id"}, "avg": {"$avg": "$host_id"}, "count": {"$sum": 1}}}])
    print("Looks like: \n")
    for i in aggResult:
        print(i, '\n')

    print("Second test should look like: \n")
    print('{ "_id" : null, "min" : 26444, "max" : 730124064, "avg" : 370354766.84915775, "count" : 147936 } \n')
    aggResult = mongoDB.listingCol.aggregate([{"$unwind": "$reviews"}, {"$group": {"_id": "null", "min": {"$min": "$reviews.id"}, "max": {"$max": "$reviews.id"}, "avg": {"$avg": "$reviews.id"}, "count": {"$sum": 1}}}])
    print("Looks like: \n")
    for i in aggResult:
        print(i, '\n')


if __name__ == "__main__":
    main()