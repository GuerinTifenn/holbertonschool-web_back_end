#!/usr/bin/env python3
""" 12-main """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    n_logs = nginx_collection.count_documents({})
    print("{} logs".format(n_logs))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_checks = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status_checks))
