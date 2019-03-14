# -*- coding: utf-8 -*-
import scrapy
from ..items import MaitianItem
import lxml
from lxml import html

class MaitianSpider(scrapy.Spider):
    #爬虫名字
    name = 'maitian'

    #爬取范围
    allowed_domains = ['maitian.cn']

    #开始地址
    start_urls = ['http://bj.maitian.cn/zfall']

    #解析
    def parse(self, response):
        item_list = response.xpath('//div[@class="list_wrap"]/ul/li[@class="clearfix"]')
        item = MaitianItem()
        for item_maitian in item_list:
            item['name'] = item_maitian.xpath('div[@class="list_title"]/h1/a/text()').extract()[0].strip()
            item['size'] = item_maitian.xpath('div[@class="list_title"]/p/span/text()').extract_first()
            item['address'] = item_maitian.xpath('div[@class="list_title"]/p[@class="house_hot"]/span/text()').extract()[0].strip()
            yield item
