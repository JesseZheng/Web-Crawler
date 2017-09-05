# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib import request
from urllib.parse import quote
import os,string,re,urllib.parse

# 豆瓣图片爬虫

class SpiderMain(object):


    # 获取该页面上单独图片页面的链接
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        reg = r"https://movie.douban.com/celebrity/" + page_url.split('/')[4] + r"/photo/\d+/$"      #正则表达式
        links = soup.find_all('a', href=re.compile(reg))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    # 爬图片开始喽
    def crawl(self, root_url, dir_name):

        dirIsExist = os.path.exists(os.getcwd() + r'\\douban\\%s'%dir_name)       #该文件夹是否存在
        if not dirIsExist:
            os.makedirs(os.getcwd() + r'\\douban\\%s'%dir_name)         #创建图片文件夹
        os.chdir(os.path.join(os.getcwd(), r'douban\\%s'%dir_name))     #进入该文件夹

        n = 1          #图片数量
        page = 0       #图片页码

        while page < 1:
            url_ = quote(root_url + "?start=%d" % (page*40), safe=string.printable)

            html_cont = request.urlopen(url_).read().decode("utf-8")

            soup = BeautifulSoup(html_cont, 'html.parser')

            urls = self._get_new_urls(url_, soup)

            for url in urls:
                pic_name = str(n) + '.jpg'
                img_url = "https://img1.doubanio.com/view/photo/photo/public/p" + url.split('/')[6] + ".jpg"
                request.urlretrieve(img_url,pic_name)
                print("Crawl " + str(n) + " : " + img_url)
                n += 1
            page += 1

        print("Crawl succeed !")


if __name__=="__main__":
    root_url = "https://movie.douban.com/celebrity/1274224/photos/"         #只需修改该影人的豆瓣ID
    dir_name = "周冬雨"                                                     #文件夹名称
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url, dir_name)