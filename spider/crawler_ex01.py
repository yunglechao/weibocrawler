# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:59:19 2015

@author: YungLeChao
"""

import urllib
import urllib.request as urllib2
import re

url = "http://www.heibanke.com/lesson/crawler_ex01/"
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'  
headers = {'User-Agent' : user_agent, 
           'Referer': 'http://www.heibanke.com/lesson/crawler_ex01/'}
pwd =0
item=['密码错误']
while item[0]=='密码错误' :
    values = {'csrfmiddlewaretoken': 'GOZ4tPUaQx77KC1m9xQbuaEZwRfGCABL', 
              'username':'reg', 
              'password':str(pwd)}
    data = urllib.parse.urlencode(values)
    binary_data = data.encode('utf-8')
    request = urllib2.Request(url=url, data=binary_data, headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<h3>.*?的(.*?), .*?</h3>', re.S)
    item = re.findall(pattern,content)
    print(item[0],pwd)
    pwd +=1