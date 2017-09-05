# -*- coding: utf-8 -*-
from baike_spider import url_manager,html_downloader,html_outputer,html_parser

class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, root_url):
        count = 1       #爬虫计数

        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print('crawl %d : %s' %(count, new_url))
            html_cont = self.downloader.download(new_url)
            new_url, new_data = self.parser.parse(new_url, html_cont)
            self.urls.add_new_urls(new_url)
            self.outputer.collect_data(new_data)

            if count == 100:
                break
            count = count + 1

        self.outputer.output_html()

if __name__=="__main__":
    root_url = "https://baike.baidu.com/item/里奥·梅西"
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url)