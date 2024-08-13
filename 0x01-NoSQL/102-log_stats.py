#!/usr/bin/env python3
""" 102-log_stats """

from pymongo import MongoClient

def print_nginx_stats():
    """ Prints statistics about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Total number of documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Count the number of methods
    methods_count = collection.aggregate([
        {"$group": {"_id": "$method", "count": {"$sum": 1}}}
    ])
    
    methods = {"GET": 0, "POST": 0, "PUT": 0, "PATCH": 0, "DELETE": 0}
    for method in methods_count:
        if method["_id"] in methods:
            methods[method["_id"]] = method["count"]

    print("Methods:")
    for method, count in methods.items():
        print(f"\tmethod {method}: {count}")

    # Count the number of documents where method=GET and path=/status
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

    # Top 10 IP addresses
    ip_counts = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    print("IPs:")
    for ip in ip_counts:
        print(f"\t{ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    print_nginx_stats()
