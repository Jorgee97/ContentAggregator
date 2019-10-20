# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.exceptions import DropItem
from datetime import datetime

class CaScrapyPipeline(object):
    def __init__(self, mongo_server, mongo_port, mongo_db, mongo_collection):
        self.mongo_server = mongo_server
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_server = crawler.settings.get('MONGODB_SERVER'),
            mongo_port = crawler.settings.get('MONGODB_PORT'),
            mongo_db = crawler.settings.get('MONGODB_DB'),
            mongo_collection = crawler.settings.get('MONGODB_COLLETION')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_server, self.mongo_port)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        item.setdefault('date', str(datetime.now().date())) 
        self.db[self.mongo_collection].insert(dict(item))
        return item

