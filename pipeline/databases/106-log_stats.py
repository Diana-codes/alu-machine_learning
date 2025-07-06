#!/usr/bin/env python3
"""
Provides statistics on Nginx logs stored in a MongoDB collection.
Prints:
- Total log count
- Method counts (GET, POST, PUT, PATCH, DELETE)
- Count of status checks
- Top 10 IPs by occurrence
"""

from pymongo import MongoClient

def log_stats():
    """
    Connects to MongoDB and prints stats about the nginx collection.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    print(f"{collection.count_documents({})} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

    print("IPs:")
    top_ips = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    log_stats()
