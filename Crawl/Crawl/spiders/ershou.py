# -*- coding: utf-8 -*-
import scrapy
# 链接提取器
from scrapy.linkextractors import LinkExtractor

# 继承关系
from scrapy.spiders import CrawlSpider, Rule

# 1.自动提取链接（符合规则的rule）

# 2.自动发送请求对象获取 response

# crawspider 默认提取url 自动去重

class ErshouSpider(CrawlSpider):
    name = 'ershou'
    allowed_domains = ['maitian.cn']
    start_urls = ['http://bj.maitian.cn/esfall']

    # 提取规则
    #1. linkExtract
    #2. callback 回调函数 解析数据
    #3. follow 是否跟进 false 不跟进


    rules = (
        Rule(LinkExtractor(allow=r'PG\d+'), callback='parse_item', follow=True),
    )

    # 解析方法
    def parse_item(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        print('###' * 50)
        print(response.url)

