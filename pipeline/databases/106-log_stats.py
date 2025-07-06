#!/usr/bin/env python3
from pymongo import MongoClient

client = MongoClient()
db = client.logs
nginx = db.nginx

print(f"{nginx.count_documents({})} logs")
print("Methods:")
for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
    count = nginx.count_documents({'method': method})
    print(f"\tmethod {method}: {count}")

status_check = nginx.count_documents({'method': 'GET', 'path': '/status'})
print(f"{status_check} status check")

print("IPs:")
pipeline = [
    {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 10}
]
for doc in nginx.aggregate(pipeline):
    print(f"\t{doc['_id']}: {doc['count']}")
