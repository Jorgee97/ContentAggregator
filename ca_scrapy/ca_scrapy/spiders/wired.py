import scrapy
from scrapy import Selector
from ca_scrapy.items import CaScrapyItem

class WiredSpider(scrapy.Spider):
    name = "wired"
    start_urls = ["https://www.wired.com/",]

    def parse(self, response):
        for article in response.css('li.post-listing-list-item__post'):
            item = CaScrapyItem()
            item['source'] = "wired.com"
            item['url'] = "http://wired.com" + article.css('a.post-listing-list-item__link::attr(href)').get()
            item['article_name'] = article.css('h5.post-listing-list-item__title::text').get() 
            yield item

