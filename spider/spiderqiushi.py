# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:53:08 2015

@author: YungLeChao
"""


import urllib
import urllib.request as urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?class="author.*?<a.*?<img.*?<h2>(.*?)</h2>.*?<div.*?'+
    'class="content">(.*?)<!--.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>.*?class="number">(.*?)</i>', re.S)
    items = re.findall(pattern,content)
    for item in items:
        havImg = re.search("img", item[2])
        if not havImg:
            print(item[0], item[1],item[3],item[4])
except urllib2.URLError as e:
    if hasattr(e,"code"):
        print (e.code)
    if hasattr(e,"reason"):
        print (e.reason)