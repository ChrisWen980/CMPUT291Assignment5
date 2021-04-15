'''
CMPUT 291
Winter 2021
Ahmad Amin 1623338
Chris  Wen 1619368
'''

from pymongo import MongoClient
import time

def main():    
    print("Task 4: Find which listed property(ies) has(have) not received any review, order them by listing_id and output the top 10")

    # Setup
    mongo_client = MongoClient()
    mongoDB = mongo_client['A5db']
    listingCol = mongoDB['listingCol']

    reviewsidList = []

    # Perform the task
    startTime = time.time()
    # Create a list of all the listing_ids
    findResult = list(mongoDB.listingCol.find({}, {"reviews.listing_id": 1}))

    for i in range(len(findResult)):
        for j in range(len(findResult[i]["reviews"])):
            if len(findResult[i]["reviews"][j]) != 0:
                reviewsidList.append(findResult[i]["reviews"][j]["listing_id"])

    # Run the query
    newFindResult = mongoDB.listingCol.find({"id": {"$nin": reviewsidList}}, {"name": 1,"id": 1}).sort("id", 1).limit(10)
    endTime = time.time()

    # Print the result
    print("Format: name, id")
    for row in newFindResult:
        print(row["name"], row["id"], sep=', ')

    # Print the running time
    print("Time taken to execute query (including id list creation): {} ms".format((endTime - startTime)*10**3))

if __name__ == "__main__":
    main()