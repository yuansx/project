#!/usr/bin/env python
#-*- coding: utf-8 -*-

from time import time
from threading import Thread
import requests

class DownloadHandler(Thread):
    def __init__(self, url):
        super().__init__()
        self._url = url

    def run(self):
        filename = self._url[self.url.rfind('.') + 1:]
        rsp = requests.get(self._url)
        with open(filename, 'wb') as f:
            f.write(rsp.content)

def download_image():
    #rsp = requests.get('http://api.tianapi.com/meinv/?key=APIKey&arename={0}'.format(u'湖北'))
    rsp = requests.get('http://www.baidu.com')
    #data = rsp.json()
    print(rsp)
    #for mm_dict in data['newslist']:
    #    url = mm_dict['picUrl']
    #    DownloadHandler(url).start()


if __name__ == '__main__':
    download_image()

