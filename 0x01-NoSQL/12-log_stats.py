#!/usr/bin/env python3
"""
12-log_stats.py
This script provides statistics about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

def main():
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Get the total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Define the methods we are interested in
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    
    # Print methods statistics
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Print status check statistics
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    main()
