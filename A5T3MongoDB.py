from pymongo import MongoClient
import time

def main():
    print("Task 3: Find how many listings each host own, ordering the output by host_id and only output the top 10")

    mongo_client = MongoClient()
    mongoDB = mongo_client['A5db']
    listingCol = mongoDB['listingCol']

    startTime = time.time()
    aggResult = mongoDB.listingCol.aggregate([{"$group": {"_id": "$host_id", "count": {"$sum": 1}}}, {"$sort": {"_id":1}}, {"$limit": 10}])
    endTime = time.time()

    print("(host_id, numListings)")
    for row in aggResult:
       print(row["_id"], row["count"])

    print("Time taken to execute query: {} ms".format((endTime - startTime)*10**3))

if __name__ == "__main__":
    main()