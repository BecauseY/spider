# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyfirstItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #图片链接
    piclink=scrapy.Field()
    #图片名字
    picname=scrapy.Field()
    #图片作者
    picauthor=scrapy.Field()
