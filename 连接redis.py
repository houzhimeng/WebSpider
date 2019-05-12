
import requests
import pymongo
import redis
from lxml import html

# connection = pymongo.MongoClient()
# db = connection.Chapter6
# handler = db.white
#
# client = redis.StrictRedis(host='127.0.0.1',port=6379,password='123456')
#
# source = requests.get('http://dongyeguiwu.zuopinj.com/5525').content
# selector = html.fromstring(source)
#
# url_list = selector.xpath('//div[@class="book_list"]/ul/li/a/@href')
# for url in url_list:
#     client.lpush('url_queue', url)
#
# #存到mongo中
# content_list = []
# while client.llen('url_queue') > 0:
#     url = client.lpop('url_queue').decode()
#     source = requests.get(url).content
#
#     selector = html.fromstring(source)
#     chapter_name = selector.xpath('//div[@class="h1title"]/h1/text()')[0]
#     content = selector.xpath('//div[@id="htmlContent"]/p/text()')
#     content_list.append({'title': chapter_name, 'content': '\n'.join(content)})
#
# handler.insert(content_list)

client = redis.Redis(host='127.0.0.1',port=6379,password='123456')
client.lpush('hzm','456','789')
print(client.llen('hzm'))
# for key in client.keys():
#     print(key.decode())
