#!/usr/bin/env python2.7
# _*_ coding: utf-8 _*_ 
# from twisted.enterprise import adbapi
import sys
 
import MySQLdb
import MySQLdb.cursors
 
import urllib
import urllib2
 
class Mysql:
 
    def __init__(self):
        self.conn = MySQLdb.connect(
            host = 'localhost',
            user = 'root',
            passwd = '',
            db = 'tuoniao_v3_test',
            charset = 'utf8',
            use_unicode = True,
        )
        self.res_list = []
 
    def check(self, url):
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("select count(*) as c from scrapy_article where link = '" + url + "'")
            res = cur.fetchone()
            res_count = res['c']
            if res_count <  1:
                return True
