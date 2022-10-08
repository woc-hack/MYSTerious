import pymongo
import bson


client = pymongo.MongoClient("mongodb://da1.eecs.utk.edu/")
db = client ['WoC']
coll = db['A_metadata.U']

dataset = coll.find({"$and": [ { "NumProjects":{"$gt":10} }, {'Gender':'female'}]},{"_id":0, "NumProjects": 1}, no_cursor_timeout=True)

print(dataset)

for record in dataset:
        print(record)

dataset.close()
