# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 11:33:05 2015

@author: YungLeChao
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import weiboLogin
import urllib
import urllib.request as urllib2

username = 'yourID'
pwd = 'passwd'

WBLogin = weiboLogin.weiboLogin()
WBLogin.login(username, pwd)
