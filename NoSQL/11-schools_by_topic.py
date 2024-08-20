#!/usr/bin/env python3
""" Find schools by topic """

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """ Find schools by topic """
    return list(mongo_collection.find({ "topics": topic }))

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    python_schools = schools_by_topic(school_collection, "Python")
    for school in python_schools:
        print(f"[{school.get('_id')}] {school.get('name')}")
