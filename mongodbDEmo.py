import pymongo

client=pymongo.MongoClient(host='localhost')
db=client['test']
db['test'].insert({'k':123})