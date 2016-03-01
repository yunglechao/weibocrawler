# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:53:08 2015

@author: YungLeChao
"""

import urllib
import urllib.request as urllib2
import http.cookiejar
import os,re,time

_url_zhihu='http://www.zhihu.com'
_url_email_login=_url_zhihu+'/login/email'
_captcha_site=_url_zhihu+'/captcha.gif'
_header={'Host':'www.zhihu.com',
'Origin':'http://www.zhihu.com',
'Pragma':'no-cache',
'Referer':'http://www.zhihu.com/',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
'X-Requested-With':'XMLHttpRequest','Accept':'*/*',
'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Content-Length':'111'}


def getXSRF(data):
    '''
    从返回的文件中使用正则表达式解析出_xsrf
    可以考虑使用BeautifulSoup
    '''
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]

def get_xsrf_opener(head):
    '''
    接受header字典,并返回构造好的opener和解析出的_xsrf
    '''
    cookie=http.cookiejar.CookieJar()
    handler=urllib2.HTTPCookieProcessor(cookie)
    opener=urllib2.build_opener(handler)
    response=opener.open(_url_zhihu)
    xsrf=getXSRF(response.read())
    with open('xsrf','w') as f:
        f.write(xsrf)
    header=[]
    for key,value in head.items():
        elme=(key,value)
        header.append(elme)
    opener.addheaders=header
    return xsrf,opener

def get_captcha_url():
    return _captcha_site+str(int(time.time())*1000)

def get_captcha(url):
    request=urllib2.Request(url)
    response=urllib2.urlopen(url)
    with open('captcha.gif','wb') as f:
        f.write(response.read())

def login(opener,xsrf='',email='',password='',captcha='',rememberme='true'):
    '''
    用来登录知乎的程序,包括返回的xsrf,email,password
    '''
    values={'email':email,'password':password,'captcha':captcha,'rememberme':rememberme,'_xsrf':xsrf}
    data=urllib.urlencode(values)
    request=urllib2.Request(_url_email_login,data)
    response=opener.open(request)
    return response.read()

def _init():
    '''
    主程序
    '''
    email=input('email: ')
    password=input('password: ')
    xsrf,opener=get_xsrf_opener(_header)
    get_captcha(_captcha_site)
    captcha=input('captcha:')
    f=login(opener,xsrf,email,password,captcha)
    print (f)


if __name__ == '__main__':
    _init()
