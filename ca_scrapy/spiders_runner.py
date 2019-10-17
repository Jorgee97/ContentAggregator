import scrapy
from scrapy.crawler import CrawlerProcess
from ca_scrapy.spiders import verge, wired

process = CrawlerProcess()
process.crawl(verge.VergeSpider)
process.crawl(wired.WiredSpider)
process.start()
