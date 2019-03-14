# -*- coding: utf-8 -*-
import scrapy
from ..items import MaitianItem,MaitianDetailItem

class MaitianSpider(scrapy.Spider):
    name = 'maitian'
    allowed_domains = ['maitian.cn']
    page = 1
    url = 'http://bj.maitian.cn/zfall/R2C4/PG{}'
    start_urls = [url.format(page)]

    # 解析列表页
    def parse(self, response):
        room_list = response.xpath('//div[@class="list_wrap"]/ul/li/div[@class="list_title"]')

        # 如果没有数据就不在循环
        if not room_list:
            return

        # 遍历所有房子信息
        for room in room_list:
            item = MaitianItem()
            item['info'] = room.xpath('./h1/a/text()').extract()[0].strip()
            detail_url = 'http://bj.maitian.cn' + room.xpath('./h1/a/@href').extract()[0].strip()
            item['size'] = room.xpath('./p//text()').extract()
            item['price'] = room.xpath('./div//text()').extract()
            yield item

            # 发送详情页请求
            yield scrapy.Request(
                detail_url,
                callback=self.parse_detail
            )


        # 循环所有内容抓取
        # self.page += 1
        # url = self.url.format(self.page)
        # yield scrapy.Request(
        #     url,
        #     callback=self.parse
        #
        # )

    # 解析详情页
    def parse_detail(self,response):
        item = MaitianDetailItem()
        item['shoufu'] = response.xpath('/html/body/section[2]/div[1]/table/tbody/tr[4]/td[2]/text()').extract()[0]
        yield item


        # with open('detail.html', 'wb') as f:
        #     f.write(response.body)