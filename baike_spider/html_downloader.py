# -*- coding: utf-8 -*-

from urllib import request
from urllib.parse import quote
import string

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        url_ = quote(url, safe=string.printable)
        response = request.urlopen(url_)

        if response.getcode() != 200:
            return None

        return response.read().decode("utf-8")