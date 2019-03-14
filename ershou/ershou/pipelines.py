# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonItemExporter
from .items import MaitianItem,MaitianDetailItem

class ErshouPipeline(object):
    def open_spider(self,spider):
        self.file = open('maitian.json','wb')
        self.exporter = JsonItemExporter(self.file)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        if isinstance(item,MaitianItem):
            self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.exporter.finish_exporting()
        self.file.close()

class ErshouDetailPipeline(object):
    def open_spider(self,spider):
        self.file = open('mdetail.json','wb')
        self.exporter = JsonItemExporter(self.file)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        if isinstance(item, MaitianDetailItem):
            self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.exporter.finish_exporting()
        self.file.close()
