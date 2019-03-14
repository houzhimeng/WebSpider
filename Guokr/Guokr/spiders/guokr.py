# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import GuokrItem

class GuokrSpider(CrawlSpider):
    name = 'guokr'
    allowed_domains = ['guokr.com']
    start_urls = ['https://www.guokr.com/ask/highlight/?page=1']

    rules = (
        # 1. 抓取列表页
        Rule(LinkExtractor(allow='page=\d+'), follow=True),

        # 2. 抓取详情页 解析数据
        Rule(LinkExtractor(allow=r'question'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        # i = {}
        # #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # #i['name'] = response.xpath('//div[@id="name"]').extract()
        # # #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        item = GuokrItem()
        # item['question'] = response.css('#articleTitle::text').extract_first()
        item['question'] = response.xpath('//h1[@id="articleTitle"]/text()').extract_first()
        # item['answer'] = response.css('.answer-txt p::text').extract_first()
        item['answer'] = response.xpath('//div[@class="answer-txt answerTxt gbbcode-content"]/child::p/text()').extract()
        yield item
