#!/usr/bin/env python2.7
# _*_ coding: utf-8 _*_ 
# from twisted.enterprise import adbapi
import sys
 
import MySQLdb
import MySQLdb.cursors
 
import urllib
import urllib2
 
import hashlib
# import httplib
# import json
 
# from util.file import FileWriter
 
# g_count = 0
 
class Tuoniao:
 
    def __init__(self, domain):
        self.conn = MySQLdb.connect(
            host = 'localhost',
            user = 'root',
            passwd = '',
            db = 'scrapy',
            charset = 'utf8',
            use_unicode = True,
        )
        self.res_list = []
        self.domain = domain
 
    def get_mysql_data(self):
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM article")
            rows = cur.fetchall()
            # print rows
            # sys.exit(0)
            for row in rows:
                article = dict(
                    title = row['title'],
                    sub_title = row['title'],
                    summary = row['summary'],
                    content = row['content'] + "<p><a href='" + row['link'] + "'>查看原文</a></p>",
                    author = row['author'],
                    date_wrote = row['date_wrote'],
                    image = row['image'],
                    status = row['status'],
                    tags = row['tags'],
                    date_added = row['date_added'],
                    link = row['link'],
                )
                res = self.post_list(article)
                self.res_list.append(res)        
            return self.res_list
 
    def post_list(self, data):
        url = self.domain + '/api/mobile/v2/index.php?route=catalog/article/addArticle'
 
        post_data = urllib.urlencode(data)
        headers = {
            'TNID': '123',
            'TNPD': self.md5('456')
        }
        req = urllib2.Request(url, post_data, headers)
        response = urllib2.urlopen(req)
        content = response.read()
        return content
 
    def md5(self, str):
        m = hashlib.md5()   
        m.update(str)
        return m.hexdigest()
 
if __name__ == '__main__':
    print 'start'
    huxiu = Tuoniao('http://tnfm.siteilex.com/')
    # huxiu = Tuoniao('http://localhost/tuoniao')
    res = huxiu.get_mysql_data()
    print res
    print 'end'
