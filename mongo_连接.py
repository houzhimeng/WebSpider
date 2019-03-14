import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
database_names = client.database_names()
db = client['test3']
# collection = db['houzhimeng']
# data = [{'id': '1', 'name':'hou', 'age':'20'},
# {'id': '3', 'name': 'wang', 'age': '30'},
# {'id': '4', 'name': 'li', 'age': '40'},
# ]
result = db.get_collection('houzhimeng').insert_many([
    {'id':'5','name':'iii','age':'24'}
])

# result = collection.insert(data)
print(result)

# content = collection.find({'age':'30'})
# print(content)