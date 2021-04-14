from pymongo import MongoClient
import time

def main():
    print('Task 6: Increase the rental cost/night by 10% for all properties in a neighbourhood given at run-time (e.g., using command line prompt or via an application parameter)')
    print("Type in the desired neighbourhood to change values for: ")
    neighbourhood = str(input())

    mongo_client = MongoClient()
    mongoDB = mongo_client['A5db']
    listingCol = mongoDB['listingCol']

    aggResult = mongoDB.listingCol.find("$neighbourhood":neighbourhood)

    startTime = time.time()
    aggResult = mongoDB.listingCol.aggregate([{"$group": {"_id": "$host_id", "count": {"$sum": 1}}}, {"$sort": {"_id":1}}, {"$limit": 10}])
    endTime = time.time()

    print("(host_id, numListings)")
    for row in aggResult:
       print(row["_id"], row["count"])

    print("Time taken to execute query: {} ms".format((endTime - startTime)*10**3))

if __name__ == "__main__":
    main()