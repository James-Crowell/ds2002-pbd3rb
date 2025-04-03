from pymongo import MongoClient, errors
from bson.json_util import dumps
import os

# Connect to database
MONGOUSER = os.getenv('MONGOUSER')
MONGOPASS = os.getenv('MONGOPASS')
MONGOHOST = os.getenv('MONGOHOST')
client = MongoClient(MONGOHOST, username=MONGOUSER, password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)

db = client.pbd3rb

# Create new collection
lab6 = db.lab6

# New documents
record_1 = {
    "name": {
        "first": "james",
        "middle": "w",
        "last": "crowell"
    },
    "id": "pbd3rb",
    "age": 19,
    "classes": ["ds2002", "cs3130"]
}

record_2 = {
    "name": {
        "first": "john",
        "last": "smith"
    },
    "id": "abc123",
    "age": 23,
    "classes": ["ds2002", "cs1000", "ds3000"]
}

record_3 = {
    "name": {
        "first": "jack",
        "middle": "w",
        "last": "lee"
    },
    "id": "dda31f",
    "age": 20,
    "classes": ["ds2002", "cs3130"]
}

record_4 = {
    "name": {
        "first": "miles",
        "middle": "w",
        "last": "bradley"
    },
    "id": "33afcd",
    "age": 22,
    "classes": ["ds2002"]
}

record_5 = {
    "name": {
        "first": "joshua",
        "middle": "w",
        "last": "smith"
    },
    "id": "fda3df",
    "age": 22,
    "classes": ["cs3130"]
}

# Insert documents
lab6.insert_many([record_1, record_2, record_3, record_4, record_5])

# Find and display docs 1,3,5
doc = lab6.find({
    "name.middle": "w",
    "classes": { "$in": ["ds2002"]}
})
print(dumps(doc, indent=2))


# Clear collection
lab6.delete_many({})