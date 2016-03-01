# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:25:04 2015

@author: YungLeChao
"""

import urllib
import urllib.request as urllib2
import re

url = "http://www.heibanke.com/lesson/crawler_ex00/"
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'  
headers = {'User-Agent' : user_agent, 
           'Referer': 'http://www.heibanke.com/lesson/crawler_ex00/'}
#values = {'wvr': '5', 'lf':'reg'}
#data = urllib.parse.urlencode(values)
#binary_data = data.encode('utf-8')
#
#geturl = url + "?" + data 
request = urllib2.Request(url,headers = headers)
response = urllib2.urlopen(request)
content = response.read().decode('utf-8')
pattern = re.compile('<h3>.*?数字(.*?)</h3>', re.S)
items = re.findall(pattern,content)
while items[0] :
    cur_url = url + str(items[0])
    request = urllib2.Request(cur_url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<h3>.*?数字是(.*?). .*?</h3>', re.S)
    items = re.findall(pattern,content)
    print(items[0])
