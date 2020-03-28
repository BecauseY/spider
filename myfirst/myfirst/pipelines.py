# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import requests

class MyfirstPipeline(object):
    def process_item(self, item, spider):
        # 模拟浏览器
        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
        headers = {'user-agent': 'Mozilla/5.0'}
        # 使用request模块，发送get请求
        r = requests.get(url=item['piclink'], headers=headers, timeout=4)

        # 下载图片，存储在本地文件目录下
        with open(r'C:\\Users\\12943\\Desktop\\信息内容安全\\实验\\实验1-爬虫\\myfirst_result\\' + item['picname'] +'_'+item['picauthor']+ '.'+item['piclink'].split(".")[-1], 'wb') as f:
            f.write(r.content)

