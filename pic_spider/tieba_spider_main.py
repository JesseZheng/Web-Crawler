# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib import request
from urllib.parse import quote
import os,string,re

# 贴吧图片爬虫

class SpiderMain(object):

    def crawl(self, root_url):
        os.chdir(os.path.join(os.getcwd(), 'photos'))
        page = 1       #贴吧页码
        n = 1          #照片数量
        url_ = quote(root_url, safe=string.printable)       #url中文处理

        while page < 27:
            html_cont = request.urlopen(url_ + "?pn=%d" % page).read().decode("utf-8")

            soup = BeautifulSoup(html_cont, 'html.parser')

            for img in soup.find_all('img', class_='BDE_Image'):
                pic_name = str(n) + '.jpg'
                img_src = img.get('src')
                request.urlretrieve(img_src, pic_name)
                print("Crawl " + str(n) + " : " + img_src)
                n += 1

            page += 1

if __name__=="__main__":
    root_url = "http://tieba.baidu.com/p/4717097958"
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url)