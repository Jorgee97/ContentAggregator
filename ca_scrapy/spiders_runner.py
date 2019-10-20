import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.settings  import Settings
from ca_scrapy.spiders import verge, wired
from ca_scrapy import settings

crawler_settings = Settings()
crawler_settings.setmodule(settings)
process = CrawlerProcess(settings=crawler_settings)
process.crawl(verge.VergeSpider)
process.crawl(wired.WiredSpider)
process.start()
