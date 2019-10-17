import scrapy
from scrapy import Selector
from ca_scrapy.items import CaScrapyItem

class VergeSpider(scrapy.Spider):
    name = "verge"
    def start_requests(self):
        urls = ["https://www.theverge.com/",]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        for article in response.css('a[data-analytics-link="article"]').getall():
            article = Selector(text=article)

            item = CaScrapyItem()
            item['source'] = "theverge.com"
            item['url'] = article.xpath('//a/@href').get()
            item['article_name'] = article.css('a::text').get()
            yield item
