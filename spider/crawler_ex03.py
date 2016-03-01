# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 16:10:38 2015

@author: YungLeChao
"""

import threading, time
import urllib
import urllib.request as urllib2
import re

url = "http://www.heibanke.com/lesson/crawler_ex03/"
pw_list_url = url + "/pw_list/?page=2"
dict1 = {}
itera_num = 0
password = ''

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'  
headers = {'User-Agent' : user_agent, 
           'Referer': 'http://www.heibanke.com/lesson/crawler_ex03/pw_list/', 
           'Cookie': 'sessionid=j3p5x5xxoyjgj6fgbamfl9zz2qcc5ngq; csrftoken=t1NFpukqLjNLA5qPzNYDt50EcRxUxDxL'}
while len(dict1)<100 :
    try :
        request = urllib2.Request(url=pw_list_url, headers = headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        pattern = re.compile('password_pos">(.*?)</td>.*?password_val">(.*?)</td>', re.S)
        pw_table = re.findall(pattern,content)
        for item in pw_table:
            dict1.update({item[0]:item[1]})
        itera_num +=1
        print(itera_num)
    except urllib2.URLError as e:
        if hasattr(e,"code"):
            print (e.code)
        if hasattr(e,"reason"):
            print (e.reason)
    finally:
        print("已经操作了%d次，但是失败了，找到了%d个密码"%(itera_num, len(dict1)))

for i in range(1, 101) :
    password = password + str(dict1.get(i))
print(password)
    