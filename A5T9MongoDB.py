'''
CMPUT 291
Winter 2021
Ahmad Amin 1623338
Chris  Wen 1619368
'''

from pymongo import MongoClient
import time
import sqlite3

def main():    
    print('Task 9: Find the top 3 listings which have reviews most similar to a set of keywords given at run-time (e.g., using command line prompt or via an application parameter). Assume those keywords will be given in a comma separated string such as "nice, inexpensive, quiet".')
    print("Type in the desired keywords: ")
    # Take in input and turn it into a string
    desiredKeywords = list(map(str, input().split(", ")))
    keywordsString = " ".join(str(word) for word in desiredKeywords)

    # Setup
    mongo_client = MongoClient()
    mongoDB = mongo_client['A5db']
    conn = sqlite3.connect('A5.db')
    c = conn.cursor()

    # Select necessary data from SQL database
    c.execute("SELECT comments FROM Reviews ORDER BY listing_id ASC;")
    reviewsData = c.fetchall()

    # Setup the collection
    try:
        reviewsCol = mongo_client.mongoDB.create_collection('reviewsCol')
    except:
        reviewsCol = mongoDB['reviewsCol']
        reviewsCol.drop()

    # Start of the task
    startTime = time.time()
    
    # Create the collection of review comments using the SQL database
    print("\nCreating collection of review comments... \n")
    for i in range(len(reviewsData)):
        insertionDict = {"review_comments": reviewsData[i][0]}
        reviewsCol.insert_one(insertionDict)

    mongoDB.reviewsCol.drop_indexes()

    # Run the query
    print("Starting query... \n")
    mongoDB.reviewsCol.create_index([("review_comments", "text")], name = "comments_index")
    searchResult = mongoDB.reviewsCol.find({"$text": {"$search": keywordsString}}, {"review_comments": 1, "score": {"$meta": "textScore"}}).sort([("score", {"$meta": "textScore"})]).limit(3)
    endTime = time.time()

    # Print the results of the query
    i = 1
    for row in searchResult:
        print("This is comment ", i, ": ", row["review_comments"])
        print("This is the score for comment ", i, ": ", row["score"], "\n")
        i += 1

    # Drop the indexes and collection
    print("Dropping indexes and collections... \n")
    mongoDB.reviewsCol.drop_indexes()
    reviewsCol.drop()

    # Print the running time
    print("Time taken to execute query (including collection and index creation): {} ms".format((endTime - startTime)*10**3))
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()