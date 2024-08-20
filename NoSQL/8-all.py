#!/usr/bin/env python3
""" List all documents in a collection """

from pymongo import MongoClient


def list_all(mongo_collection):
    """ List all documents in a collection """
    return list(mongo_collection.find())

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    for school in schools:
        print(f"[{school.get('_id')}] {school.get('name')}")
