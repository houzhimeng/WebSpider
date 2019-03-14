# encoding:utf-8
import requests, re
from bs4 import BeautifulSoup


response = requests.get('https://movie.douban.com/top250')
soup = BeautifulSoup(response.text, "lxml")

#获取电影名称
title = soup.find("span", attrs={"class": "title"}).getText()

#获取评分
rating_num = soup.find("span", attrs={"class": "rating_num"}).getText()

#获取平价
inq = soup.find("span", attrs={"class": "inq"}).getText()


print(title)
print(rating_num)