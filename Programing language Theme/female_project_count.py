import pymongo
import bson

client = pymongo.MongoClient("mongodb://da1.eecs.utk.edu/")
db = client ['WoC']
coll = db['A_metadata.U']

result = coll.find({"$and": [ { "NumProjects":{"$eq":1} }, {'Gender':'female'} ]}, no_cursor_timeout=True)

print(result.count())

dataset.close()
