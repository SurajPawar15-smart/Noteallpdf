# -*- coding: utf-8 -*-
import scrapy
#This is the basic spider we created from the command line
#I just added the 's' in the start_urls to go directly to the secure page as directed
#Note: Based on your location, amazon domain might reject you by multiple 503 responses
#That is fine we will take care of it later

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['https://amazon.com/']

    def parse(self, response):
        pass
