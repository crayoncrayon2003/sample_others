from pymongo import MongoClient
import random
import time

def main():
    # connet to mongo
    client = MongoClient("mongodb://localhost:27017")
    # connet to db
    db = client["testdb"]
    # connet to collection
    collection = db["test_collection"]

    temperature = 10
    humidity = 10
    battery  = 10

    for i in range(100):
        # update data
        data = {"temperature":temperature, "humidity":humidity, "battery": battery}
        print(data)
        collection.insert_one(data)
        temperature += random.randint(-3, 3)
        humidity += random.randint(-3, 3)
        battery += random.randint(-3, 3)
        time.sleep(2)

    client.close()

if __name__ == '__main__':
    main()