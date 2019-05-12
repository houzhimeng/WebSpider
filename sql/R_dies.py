import redis
import json
client = redis.Redis(host='127.0.0.1',port=6379,password='123456')
# print(client.keys())

# info = json.dumps({'name': '张小二', 'age': 18, 'salary': 100, 'address': '北京'})
# client.hset(info)
# client.hkeys()
# client.zincrby('hou',90,'oldage')
print(client.zrange('hou', 0, -1, desc=True, withscores=True))