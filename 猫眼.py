import requests
import re
import json
import time
import csv
from lxml import etree
import pandas as pd
import matplotlib.pyplot as plt


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def get_thumb(url):
    pattern = re.compile(r'(.*?)@.*?')
    thumb = re.search(pattern, url)
    return thumb.group(1)

def get_release_time(data):
    pattern = re.compile(r'(.*?)((|$)')
    items = re.search(pattern, data)
    if items is None:
        return '未知'
    return items.group(1)  # 返回匹配到的第一个括号(.*?)中结果即时间

def get_release_area(data):
   pattern = re.compile(r'.*((.*))')
   items = re.search(pattern, data)
   if items is None:
        return '未知'
   return items.group(1)


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'+ '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'+ '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    print(items)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }

def write_to_file3(item):
    with open('猫眼top100.csv', 'a', encoding='utf_8_sig', newline='') as f:
        # 'a'为追加模式（添加）
        # utf_8_sig格式导出csv不乱码
        fieldnames = ['index', 'image', 'title', 'actor', 'time', 'score']
        w = csv.DictWriter(f, fieldnames=fieldnames)
        # w.writeheader()
        w.writerow(item)

# def parse_one_page2(html):
#     parse = etree.HTML(html)
#     items = parse.xpath('//*[@id="app"]//div//dd')
#     # 完整的是//*[@id="app"]/div/div/div[1]/dl/dd
#     # print(type(items))
#     # *代表匹配所有节点，@表示属性
#     # 第一个电影是dd[1],要提取页面所有电影则去掉[1]
#     # xpath://*[@id="app"]/div/div/div[1]/dl/dd[1]
#     for item in items:
#         yield{
#             'index': item.xpath('./i/text()')[0],
#             #./i/text()前面的点表示从items节点开始
#             #/text()提取文本
#             'thumb': get_thumb(str(item.xpath('./a/img[2]/@src')[0].strip())),
#             # 'thumb': 要在network中定位，在elements里会写成@src而不是@src，从而会报list index out of range错误。
#             'name': item.xpath('./a/@title')[0],
#             'star': item.xpath('.//p[@class = "star"]/text()')[0].strip(),
#             'time': get_release_time(item.xpath(
#                 './/p[@class = "releasetime"]/text()')[0].strip()[5:]),
#             'area': get_release_area(item.xpath(
#                 './/p[@class = "releasetime"]/text()')[0].strip()[5:]),
#             'score' : item.xpath('.//p[@class = "score"]/i[1]/text()')[0] +
#             item.xpath('.//p[@class = "score"]/i[2]/text()')[0]
#         }

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)

    for item in parse_one_page(html):
        print(item)
        write_to_file3(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)



