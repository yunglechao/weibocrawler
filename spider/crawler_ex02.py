# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:59:19 2015

@author: YungLeChao
"""

import urllib
import urllib.request as urllib2
import re

url = "http://www.heibanke.com/lesson/crawler_ex02/"
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'  
headers = {'User-Agent' : user_agent, 
           'Referer': 'http://www.heibanke.com/lesson/crawler_ex02/', 
           'Cookie': 'sessionid=j3p5x5xxoyjgj6fgbamfl9zz2qcc5ngq; csrftoken=t1NFpukqLjNLA5qPzNYDt50EcRxUxDxL'}
pwd =30


item=['密码错误']
while item[0]=='密码错误' :
    try:
        values = {'csrfmiddlewaretoken': 't1NFpukqLjNLA5qPzNYDt50EcRxUxDxL', 
              'username':'reg', 
              'password':str(pwd)}
        data = urllib.parse.urlencode(values)
        binary_data = data.encode('utf-8')
        request = urllib2.Request(url=url, data=binary_data, headers = headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        pattern = re.compile('<h3>.*?的(.*?), .*?</h3>', re.S)
        item = re.findall(pattern,content)
        print(item[0], pwd)
        pwd -=1
    except urllib2.URLError as e:
        if hasattr(e,"code"):
            print (e.code, "密码是:", pwd)
        if hasattr(e,"reason"):
            print (e.reason)