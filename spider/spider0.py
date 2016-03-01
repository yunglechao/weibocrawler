# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:48:24 2015

@author: YungLeChao
"""
import urllib
import urllib.request as urllib2

values = {"username":"l-zhaoyl@qq.com", "access-token":"b65fe309-70d5-4bb5-ba9f-19c68ae0e4fd"}
data = urllib.parse.urlencode(values)
binary_data = data.encode('utf-8')
print(binary_data)
#user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'  
headers = {'User-Agent' : user_agent }
url = "https://passport.csdn.net/account/login?from=http%3A%2F%2Fmy.csdn.net%2Fmy%2Fmycsdn"
geturl = url + "?" +data
request = urllib2.Request(url=geturl, headers=headers)
response = urllib2.urlopen(request)
print(response.read().decode('utf-8'))
try:
    urllib2.urlopen(request)
except urllib2.URLError as e:
    print(e.reason)
