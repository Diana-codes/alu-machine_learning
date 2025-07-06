#!/usr/bin/env python3
"""
Improved script that provides stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

def log_stats():
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    print(f"{collection.count_documents({})} logs")
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(f"\tmethod {method}: {collection.count_documents({'method': method})}")
    print(f"{collection.count_documents({'method': 'GET', 'path': '/status'})} status check")

    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    for doc in collection.aggregate(pipeline):
        print(f"\t{doc['_id']}: {doc['count']}")

if __name__ == "__main__":
    log_stats()
