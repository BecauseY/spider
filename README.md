# 文件说明：

###1.requests+bs4+re.py使用 requests+bs4+re技术路线实现爬虫，含有多个例子。

###2.myfirst文件夹是一个scrapy工程，使用scrapy+xpath技术路线实现爬虫。

###3.myfirst_result文件夹存放myfirst工程爬取的结果。



#scrapy使用流程：

###1.建立工程和spider模板

scrapy startproject myfirst      建立一个工程名为myfirst 

cd  myfirst                      切换到该工程目录下

scrapy genspider mcbqb mc.163.com    建立一个爬虫，名为mcbqb，爬取mcbqb mc.163.com

###2.编写item

配置itrms.py

###3.编写spider

配置spiders/mcbqb.py文件,修改对返回页面的处理,修改对新增URL爬取请求的处理

###4.编写Pipelines

配置pipelines.py文件,定义对爬取项（Scraped Item）的处理类

###5.配置ITEM_PIPELINES选项

配置settings.py文件，配置ITEM_PIPELINES选项

###6.运行爬虫

scrapy crawl mcbqb




#另外：

###1.还有一个gooseeker可以实现爬虫，小白适用，就是操作软件的使用。官网http://www.gooseeker.com/有视频教程。

###2.关于 requests库 和 scrapy框架 各有各自的好处，可见视频说明https://www.bilibili.com/video/BV1kx411S7Fh?p=53

###3.BeautifulSoup， lxml, css, xpath, re 这些都是对返回的网页源代码进行操作的库。
