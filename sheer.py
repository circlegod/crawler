# -*- coding: utf-8 -*-
import scrapy
from sheergirl.items import SheergirlItem

class SheerSpider(scrapy.Spider):
    name = 'sheer'
    allowed_domains = ['sheergirl.com']
    offset = 3
    url = "https://www.sheergirl.com/collections/prom-dresses?page="
    start_urls = [url + str(offset)]

    def parse(self, response):
        productURL = response.xpath('//div[contains(@class, "three columns")]//div[contains(@class, "relative product_image")]/a/@href').extract()
        for URL in productURL:
            yield scrapy.Request("https://www.sheergirl.com" + URL, callback=self.parse_item)

        if self.offset <= 3:
           self.offset += 1
           yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    def parse_item(self, response):
        item = SheergirlItem()
        imageLink = response.xpath('//div[contains(@class,"gallery-cell")]/a/@href').extract()
        for i in range(0, len(imageLink)):
            item["imageLink"] = "https:" + imageLink[i]
            yield item


