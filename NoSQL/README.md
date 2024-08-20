# NoSQL Project

This project is part of the Holberton School curriculum, focusing on NoSQL databases, specifically MongoDB. The goal is to gain hands-on experience with MongoDB by performing various operations such as creating databases, inserting documents, querying collections, and more.

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without external help:

- **General Concepts**
  - What NoSQL means
  - The differences between SQL and NoSQL
  - What ACID is
  - What document storage is
  - The different types of NoSQL databases
  - The benefits of using a NoSQL database
  - How to query, insert, update, and delete information in a NoSQL database
  - How to use MongoDB effectively

## Resources

To complete this project, make sure to review the following resources:

- [NoSQL Databases Explained](https://example.com)
- [What is NoSQL?](https://example.com)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://example.com)
- [MongoDB Tutorial 2: Insert, Update, Remove, Query](https://example.com)
- [Aggregation in MongoDB](https://example.com)
- [Introduction to MongoDB and Python](https://example.com)
- [mongo Shell Methods](https://example.com)
- [The mongo Shell](https://example.com)

## Requirements

### MongoDB Command Files

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2).
- Files must end with a new line.
- The first line of each file should be a comment: `// my comment`.
- A `README.md` file at the root of the project folder is mandatory.
- The length of your files will be tested using `wc`.

### Python Scripts

- Python files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7 and PyMongo 3.10.
- Files must end with a new line.
- The first line of each Python file should be `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Your code must adhere to the `pycodestyle` style guide (version 2.5.*).
- The length of your files will be tested using `wc`.
- All modules should have documentation accessible via `python3 -c 'print(__import__("my_module").__doc__)'`.
- All functions should have documentation accessible via `python3 -c 'print(__import__("my_module").my_function.__doc__)'`.
- Your code should not execute when imported (use `if __name__ == "__main__":`).

### MongoDB Installation

To install MongoDB 4.2 on Ubuntu 18.04, follow these commands:

```bash
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
$ sudo service mongod status
$ mongo --version
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'
```

### Potential Issues

If document creation fails or you encounter the error `Data directory /data/db not found., terminating`, you can resolve it by creating the necessary directory:

```bash
$ sudo mkdir -p /data/db
```

If `/etc/init.d/mongod` is missing, please refer to the official MongoDB documentation to resolve this issue.

### Using a Container

If you prefer using a container, request one running Ubuntu 18.04 with MongoDB. Start MongoDB using:

```bash
$ service mongod start
```

## Tasks

### 0. List All Databases

Write a script that lists all databases in MongoDB.

- **Task:** Create a script that connects to the MongoDB server and lists all available databases.
- **File:** [`0-list_databases`](./0-list_databases)

### 1. Create or Use a Database

Write a script that creates a database named `my_db` or switches to it if it already exists.

- **Task:** The script should ensure that it is connected to the `my_db` database, either by creating it or using it if it already exists.
- **File:** [`1-use_or_create_database`](./1-use_or_create_database)

### 2. Insert Document

Write a script that inserts a document into the collection `school` with the attribute `name` set to "Holberton school".

- **Task:** The script should connect to a specified database and insert a document into the `school` collection.
- **File:** [`2-insert`](./2-insert)

### 3. List All Documents

Write a script that lists all documents in the collection `school`.

- **Task:** The script should retrieve and print all documents from the `school` collection of the specified database.
- **File:** [`3-all`](./3-all)

### 4. List All Matching Documents

Write a script that lists all documents where `name="Holberton school"` in the collection `school`.

- **Task:** The script should retrieve and print all documents from the `school` collection where the `name` field matches "Holberton school".
- **File:** [`4-match`](./4-match)

### 5. Count Documents

Write a script that displays the number of documents in the collection `school`.

- **Task:** The script should count and display the number of documents in the `school` collection of the specified database.
- **File:** [`5-count`](./5-count)

### 6. Update Document

Write a script that adds a new attribute `address` with the value "972 Mission street" to all documents in the `school` collection where `name="Holberton school"`.

- **Task:** The script should update all matching documents by adding the `address` field.
- **File:** [`6-update`](./6-update)

### 7. Delete by Match

Write a script that deletes all documents where `name="Holberton school"` in the `school` collection.

- **Task:** The script should delete all documents from the `school` collection where the `name` field matches "Holberton school".
- **File:** [`7-delete`](./7-delete)

### 8. List All Documents in Python

Write a Python function that lists all documents in a collection.

- **Task:** The function should return a list of all documents in a given collection. If the collection is empty, it should return an empty list.
- **Prototype:** `def list_all(mongo_collection):`
- **File:** [`8-all.py`](./8-all.py)

### 9. Insert a Document in Python

Write a Python function that inserts a new document into a collection based on keyword arguments.

- **Task:** The function should insert a document into the specified collection and return the new document’s `_id`.
- **Prototype:** `def insert_school(mongo_collection, **kwargs):`
- **File:** [`9-insert_school.py`](./9-insert_school.py)

### 10. Change School Topics

Write a Python function that changes all topics of a school document based on the name.

- **Task:** The function should update the `topics` field for the document(s) where the `name` matches the provided value.
- **Prototype:** `def update_topics(mongo_collection, name, topics):`
- **File:** [`10-update_topics.py`](./10-update_topics.py)

### 11. Find Schools by Topic

Write a Python function that returns the list of schools having a specific topic.

- **Task:** The function should find and return all documents in the collection that include the specified topic in their `topics` field.
- **Prototype:** `def schools_by_topic(mongo_collection, topic):`
- **File:** [`11-schools_by_topic.py`](./11-schools_by_topic.py)

### 12. Log Stats

Write a Python script that provides some statistics about Nginx logs stored in MongoDB.

- **Task:** The script should display:
  - The total number of logs.
  - The number of logs for each HTTP method (GET, POST, PUT, PATCH, DELETE).
  - The number of logs where the method is GET and the path is `/status`.
- **File:** [`12-log_stats.py`](./12-log_stats.py)
