# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 17:36:16 2015

@author: YungLeChao
"""

import pymysql

class MySQLConnector(object):
    """A MySQL connector class. """

    def __init__(self, user, passwd, db):
        #Connect to MySQL DB what you want to save to. 
        self.conn = pymysql.connect(user=user, 
                           passwd=passwd, 
                           host='localhost', 
                           db=db, 
                           charset='utf8')
        self.cur = self.conn.cursor()
        sql = "create table if not exists weibo(rowid int unsigned not null auto_increment, userID varchar(20) not null,homepage varchar(50) not null,post varchar(280)not null, primary key(rowid) )ENGINE=InnoDB DEFAULT CHARSET=utf8 auto_increment=1"
        self.update_DB(sql)
        #return (self.conn,self.cur)

    def update_DB(self, sql):
        #updateDB with sql script
        self.cur.execute(sql)
        self.conn.commit()

    def insert_to_Table(self, userID, homepage, post):
        #Insert to Table 'weibo',column 'userID'&'homepage'.
        sql = "insert into weibo (userID, homepage, post) values ('%s', '%s', '%s')"% (userID, homepage, post)
        self.update_DB(sql)

    def query_DB(self, sql):
        #Query sql
        self.cur.execute(sql)
        return (self.cur)

    def close_Conn(self):
        #Close the connect.
        self.cur.close()    
        self.conn.close()