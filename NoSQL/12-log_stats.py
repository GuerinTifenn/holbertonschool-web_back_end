#!/usr/bin/env python3
""" Provide stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    log_count = nginx_collection.count_documents({})
    print(f"{log_count} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = nginx_collection.count_documents({ "method": method })
        print(f"\tmethod {method}: {method_count}")

    status_count = nginx_collection.count_documents({ "method": "GET",
                                                     "path": "/status" })
    print(f"{status_count} status check")
