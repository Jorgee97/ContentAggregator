# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from datetime import datetime

class CaScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    article_name = Field()
    url = Field()
    source = Field()
    date = Field()
