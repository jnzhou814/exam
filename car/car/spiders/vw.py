# -*- coding: utf-8 -*-
import scrapy
from car.items import CarItem


class VwSpider(scrapy.Spider):
    name = 'vw'
    allowed_domains = ['car.bitauto.com']
    start_urls = ['http://car.bitauto.com/xuanchegongju/?l=8&mid=8']

    '''def parse(self,response):
        catalogues=response.selector.xpath('//span[@class="category-content"]/a/@href').extract()
        for catalogue in catalogues:
            car_catalogue_url = 'http://car.bitauto.com' + str(catalogue)
            print(car_catalogue_url)
            yield scrapy.Request(car_catalogue_url,callback=self.parse_detail)'''
            
    def parse(self, response):
        results=response.selector.xpath('//div[@class="search-result-list-item"]')
        for result in results:
            item=CarItem()
            item['car_name']=result.xpath("./a/p[@class='cx-name text-hover']/text()").extract()
            item['max_price']=result.xpath("./a/p[@class='cx-price']/text()").extract()[0].split('-')[0]
            item['min_price']=result.xpath("./a/p[@class='cx-price']/text()").extract()[0].split('-')[1][:-2]
            item['pic_src']=result.xpath("./a/img/@src").extract()
            yield item

       

        
