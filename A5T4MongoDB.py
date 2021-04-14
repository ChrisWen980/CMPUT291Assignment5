from pymongo import MongoClient
import time

def main():    
    print("Task 4: Find which listed property(ies) has(have) not received any review, order them by listing_id and output the top 10")

    mongo_client = MongoClient()
    mongoDB = mongo_client['A5db']
    listingCol = mongoDB['listingCol']

    reviewsidList = []
    findResult = list(mongoDB.listingCol.find({}, {"reviews.listing_id": 1}))

    for i in range(len(findResult)):
        for j in range(len(findResult[i]["reviews"])):
            if len(findResult[i]["reviews"][j]) != 0:
                reviewsidList.append(findResult[i]["reviews"][j]["listing_id"])

    startTime = time.time()
    newFindResult = mongoDB.listingCol.find({"id": {"$nin": reviewsidList}}, {"name": 1,"id": 1}).sort("id", 1).limit(10)
    endTime = time.time()

    print("(name, id)")

    for row in newFindResult:
        print(row["name"], row["id"], sep=', ')

    print("Time taken to execute query: {} ms".format((endTime - startTime)*10**3))

if __name__ == "__main__":
    main()