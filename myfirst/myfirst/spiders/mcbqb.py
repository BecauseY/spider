# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from myfirst.items import MyfirstItem

class McbqbSpider(scrapy.Spider):
    name = 'mcbqb'
    allowed_domains = ['mc.163.com']
    start_urls = ['http://mc.163.com/wjzp/bqb/index.html']

    def parse(self, response):
        item=MyfirstItem()
        pics=response.xpath('//ul[@class="list"]/li')
        for pic in pics:
            #提取信息
            item["piclink"] = pic.xpath('./div/img/@src').extract()[0]
            item["picname"] = pic.xpath('./div/div/p[@class="work_p3"]/text()').extract()[0]
            item["picauthor"] = pic.xpath('./div/div/p[@class="work_p4"]/text()').extract()[0]

            yield item


            #实现翻页操作
            for i in range(2, 4):
                url='http://mc.163.com/wjzp/bqb/index_'+str(i)+'.html'
                yield Request(url,callback=self.parse)

