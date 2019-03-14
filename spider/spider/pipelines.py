# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonItemExporter

class SpiderPipeline(object):
    def process_item(self, item, spider):
        with open('maitian.json', 'ab') as f:
            export = JsonItemExporter(f)
            export.start_exporting()
            export.export_item(item)
            export.finish_exporting()


