#---------------------------------------技术路线：requests+bs4+re
#####最简单框架，爬京东一个页面
# import requests
# url = "https://item.jd.com/2967929.html"
# try:
#     r=requests.get(url)
#     r.raise_for_status() #如果状态不是200，引发error异常
#     r.encoding=r.apparent_encoding
#     print(r.text[:1000])
# except:
#     print("爬取失败")


#####解决网站只让浏览器浏览，即修改user-agent，比如亚马逊的页面,不改爬不了
# import requests
# url="https://www.amazon.cn/gp/product/B01M8L523Y"
# try:
#     kv={'user-agent':'Mozilla/5.0'}
#     r=requests.get(url,headers=kv)
#     r.raise_for_status()
#     r.encoding=r.apparent_encoding
#     print(r.text[1000:2000])
# except:
#     print("爬取失败")


#####百度，360搜索请求
'''
搜索引擎关键词接口：
百度：http://www.baidu.com/s？wd=keyword
360:http://www.so.com/s？q=keyword
'''
# import requests
# keyword="Python"
# baiduurl="http://www.baidu.com/s"
# three60url="http://www.so.com/s"
# try:
#     kv={'q':keyword}  #百度的把q变为wd
#     r=requests.get(three60url,params=kv)
#     print(r.request.url)
#     r.raise_for_status()
#     print(len(r.text))
# except:
#     print("爬取失败")



#####爬取图片保存到本地
# import requests
# import os
# url="http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
# root="D://pics//"
# path= root + url.split('/')[-1]
# try:
#     if not os.path.exists(root):
#         os.mkdir(root)
#     if not os.path.exists(path):
#         r=requests.get(url)
#         with open(path,'wb') as f:
#             f.write(r.content)
#             f.close()
#             print("文件保存成功")
#     else:
#         print("文件已存在")
# except:
#     print("爬取失败")

#----------------------------稍微高级一点的---------------------------------
'''
定向爬虫（只爬取给定的url，不进行扩展）
中国大学排名网站：www.zuihaodaxue.cn
'''
# import requests
# from bs4 import BeautifulSoup
# import bs4
#
# def getHtmlText(url):
#     try:
#         r=requests.get(url)
#         r.raise_for_status()
#         r.encoding=r.apparent_encoding
#         return r.text
#     except:
#         return ""
#
# def fillUnivList(ulist,html):
#     suop=BeautifulSoup(html,"html.parser")
#     for tr in suop.find('tbody').children:
#         if isinstance(tr,bs4.element.Tag):
#             tds=tr('td')
#             ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])
#
# def printUnivList(ulist,num):
#     print("{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}".format("排名","学校名称","省市","总分",chr(12288)))
#     for i in range(num):
#         u=ulist[i]
#         print("{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}".format(u[0],u[1],u[2],u[3],chr(12288)))
#
# def main():
#     uinfo=[]
#     url='http://zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
#     html=getHtmlText(url)
#     fillUnivList(uinfo,html)
#     printUnivList(uinfo,20)#打印20所学校
#
# main()
#

'''
定向爬虫（只爬取给定的url，不进行扩展）
淘宝网站：www.taobao.cn   提取商品名称和价格
问题：通过观察url解决
1.淘宝的搜索接口
2.翻页的处理
步骤：
1：提交商品搜索请求，循环获取页面。
2：对于每个页面，提取商品名称和价格信息。
3：将信息输出到屏幕上。
'''
# import requests
# import re
#
# def getHtmlText(url):
#     try:
#         #此处加了headers相当于登陆了，不加的话会跳转到登陆界面
#         headers = {
#             "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
#             "cookie": "t=c1e8231792f007e72593175d60586f3a; cna=HthOFWZZfEoCAZkiYyMw5eUw; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; tracknick=tb313659628; lgc=tb313659628; tg=0; enc=C%2B2%2F0QsEwiUFmf00owySlc7hJiEsY4t4EIGdIzzH6ih9ajzhcMJCs7wzlX4%2B4gJrv2IlLviuxk0B1VAXlVwD8Q%3D%3D; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; miid=1314040285196636905; uc3=vt3=F8dBy3vI3wKCeS4bgiY%3D&id2=VyyWskFTTiu0DA%3D%3D&nk2=F5RGNwsJzCC9CC4%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D; _cc_=VFC%2FuZ9ajQ%3D%3D; _m_h5_tk=ec90707af142ccf8ce83ead2feda4969_1560657185501; _m_h5_tk_enc=2bc06ae5460366b0574ed70da887384e; mt=ci=-1_0; cookie2=14c413b3748cc81714471780a70976ec; v=0; _tb_token_=e33ef3765ebe5; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; swfstore=97544; JSESSIONID=80EAAE22FC218875CFF8AC3162273ABF; uc1=cookie14=UoTaGdxLydcugw%3D%3D; l=bBjUTZ8cvDlwwyKtBOCNCuI8Li7OsIRAguPRwC4Xi_5Z86L6Zg7OkX_2fFp6Vj5RsX8B41jxjk99-etki; isg=BP__g37OnjviDJvk_MB_0lRbjtNJTFLqmxNfMJHMlK71oB8imbTI1uey5jD7-Cv-"
#         }
#
#         r=requests.get(url,headers=headers)
#         r.raise_for_status()
#         r.encoding=r.apparent_encoding
#         return r.text
#     except:
#         return ""
#
# def parsePage(ilt,html):
#     try:
#         plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
#         tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
#         for i in range(len(plt)):
#             price = eval(plt[i].split(':')[1])
#             title = eval(tlt[i].split(':')[1])
#             ilt.append([price,title])
#     except:
#         print("")
#
#
# def printGoodsList(ilt):
#     print("{:4}\t{:8}\t{:30}".format("序号","价格","商品名称"))
#     count=0
#     for g in ilt:
#         count+=1
#         print("{:4}\t{:8}\t{:30}".format(count,g[0],g[1]))
#
#
# def main():
#     goods='书包'
#     depth=2 #爬取第1页和第2页
#     start_url='https://s.taobao.com/search?q='+goods
#     infoList=[]
#     for i in range(depth):
#         try:
#             url=start_url+'&s='+str(44*i)
#             html=getHtmlText(url)
#             parsePage(infoList,html)
#         except:
#             continue
#     printGoodsList(infoList)
#
# main()
















