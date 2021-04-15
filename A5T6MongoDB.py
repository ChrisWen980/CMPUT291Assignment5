'''
CMPUT 291
Winter 2021
Ahmad Amin 1623338
Chris  Wen 1619368
'''

from pymongo import MongoClient
import time

def main():
    print('Task 6: Increase the rental cost/night by 10% for all properties in a neighbourhood given at run-time (e.g., using command line prompt or via an application parameter)')
    print("Type in the desired neighbourhood to change values for: ")
    # Take the input
    neighbourhood = str(input())

    # Setup
    mongo_client = MongoClient()
    mongoDB = mongo_client['A5db']
    listingCol = mongoDB['listingCol']

    # Fetch the prices and neighbourhoods before updating
    beforeUpdate = mongoDB.listingCol.find({"neighbourhood": neighbourhood}, {"price": 1, "neighbourhood": 1})

    # Check if the neighbourhood exists
    if beforeUpdate.count() != 0:
        # Print prices and neighbourhoods before updating
        print("These are the prices before update: ")
        print("Format: price, neighbourhood")
        for row in beforeUpdate:
            print(row["price"], "  ", row["neighbourhood"])

        # Run query
        startTime = time.time()
        mongoDB.listingCol.update({"neighbourhood": neighbourhood}, {"$mul": {"price": 1.1}}, upsert = False, multi = True)
        endTime = time.time()

        # Fetch the prices and neighbourhoods after updating
        afterUpdate = mongoDB.listingCol.find({"neighbourhood": neighbourhood}, {"price": 1, "neighbourhood": 1})
        
        # Print prices neighbourhoods after updating
        print("These are the prices before update: ")
        print("Format: price, neighbourhood")
        for row in afterUpdate:
            print(row["price"], "  ", row["neighbourhood"])

        # Print running time
        print("Time taken to execute query: {} ms".format((endTime - startTime)*10**3))
    
    else:
        # Print error message
        print("This neighbourhood does not exist")

if __name__ == "__main__":
    main()