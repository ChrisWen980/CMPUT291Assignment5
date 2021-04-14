from pymongo import MongoClient
import time

def main():
    print('Task 6: Increase the rental cost/night by 10% for all properties in a neighbourhood given at run-time (e.g., using command line prompt or via an application parameter)')
    print("Type in the desired neighbourhood to change values for: ")
    neighbourhood = input()

    mongo_client = MongoClient()
    mongoDB = mongo_client['A5db']
    listingCol = mongoDB['listingCol']

    aggResult = mongoDB.listingCol.aggregate([{"$match": {"neighbourhood": neighbourhood}}])

    startTime = time.time()
    updateResult = mongoDB.listingCol.update_many("neighbourhood": aggResult, [{"_id": "null"}, {"$set": {"$multiply": ["price", 1.1]}}])
    endTime = time.time()


    print("Time taken to execute query: {} ms".format((endTime - startTime)*10**3))

if __name__ == "__main__":
    main()