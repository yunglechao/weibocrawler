# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 17:36:16 2015

@author: YungLeChao
"""

import pymysql

def connDB():
    conn = pymysql.connect(user='root', passwd='root', host='localhost', db='lesson', charset='utf8')
    cur = conn.cursor()
    sql = "create table if not exists weibo(userID varchar(20) not null,homepage varchar(50) not null,post varchar(280)not null)ENGINE=InnoDB DEFAULT CHARSET=utf8"
    updateDB(conn, cur, sql)
    return (conn,cur)

def updateDB(conn, cur, sql):
    cur.execute(sql)
    conn.commit()

def insert2Table(conn, cur,values):
    sql = "insert into weibo (userID) values ('%s')"%values
    cur.execute(sql)
    conn.commit()

def queryDB(cur, sql):
    cur.execute(sql)
    return (cur)
    
def closeConn(conn,cur):
    cur.close()    
    conn.close()