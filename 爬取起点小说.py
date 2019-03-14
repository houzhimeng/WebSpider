import requests
import time
import re
import os
from lxml import etree



class spider():
    #确定下载链接,xapth获取title，adrees,并且创建文件夹
    def start_quest(self):
        respone = requests.get("https://www.qidian.com/all")
        html = etree.HTML(respone.content.decode())
        B_title_list = html.xpath('//div[@class="book-mid-info"]/h4/a/text()')
        B_href_list = html.xpath('//div[@class="book-mid-info"]/h4/a/@href')
        # print(B_title_list,B_href_list)
        for B_title, B_href in zip(B_title_list, B_href_list):
            os.makedirs(B_title, exist_ok=True)
            self.file_data(B_href, B_title)

    def file_data(self, B_href, B_title):
        respone = requests.get("http:" + B_href)
        html = etree.HTML(respone.content.decode())
        L_title_list = html.xpath('//ul[@class="cf"]/li/a/text()')
        L_href_list = html.xpath('//ul[@class="cf"]/li/a/@href')
        for L_title, L_href in zip(L_title_list, L_href_list):
            self.finaly(L_title, L_href, B_title)

    def finaly(self, L_title, url, B_title):
        respone = requests.get("http:" + url)
        html = etree.HTML(respone.content.decode())
        text_list = html.xpath('//div[@class="read-content j_readContent"]/p/text()')
        text = "\n".join(text_list)
        file_name = B_title + "/" + L_title + ".txt"
        print("正在抓取:" + file_name)
        with open(file_name,"a", encoding="utf-8") as f:
            f.write(text)
            
spider = spider()
spider.start_quest()
