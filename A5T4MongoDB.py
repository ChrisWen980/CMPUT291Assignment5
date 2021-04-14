from pymongo import MongoClient
import time

def main():    
    print("Task 4: Find which listed property(ies) has(have) not received any review, order them by listing_id and output the top 10")

    mongo_client = MongoClient()
    mongoDB = mongo_client['A5db']
    listingCol = mongoDB['listingCol']

    reviewsidList = []
    findResult = mongoDB.listingCol.find({}, {"reviews.id": 1})

    #print(findResult[0], "\n \n \n",findResult[1]) 

    i = 0

    while findResult[i] != "":
        for j in range(len(findResult[i]["reviews"])):
            reviewsidList.append(findResult[i]["reviews"][j]["id"])
        i += 1


    startTime = time.time()
    newAggResult = mongoDB.listingCol.find({"id": {"$nin": ["$reviews.id"]}}, {"name": 1,"id": 1}).sort("id", 1).limit(10)
    #c.execute("SELECT L.name, L.id FROM Listings L WHERE NOT EXISTS (SELECT * From Reviews R WHERE L.id = R.listing_id) ORDER BY L.id ASC LIMIT 10;")
    endTime = time.time()

    print("(name, id)")

    for row in newAggResult:
        print(row)

    print("Time taken to execute query: {} ms".format((endTime - startTime)*10**3))

if __name__ == "__main__":
    main()