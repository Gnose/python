#/usr/bin/env python
#coding=utf8
import httplib
import urllib
import urllib2
import sys
# import time
import MySQLdb
import MySQLdb.cursors
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
# from newspaper import Article
# reload(sys)
# sys.setdefaultencoding('utf-8')
class Vr186:
 
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
 
    def get_mysql_data(self):     
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT title, content FROM scrapy_article")
            rows = cur.fetchall()
            # print rows
            # sys.exit(0)
            for row in rows:
                article = dict(
                    title = row['title'],
                    content = row['content'],
                )
                res = self.sends(article)
                self.res_list.append(res)        
            return self.res_list
 
 
    def sends(self, data):
        #链接WordPress，输入xmlrpc链接，后台账号密码
        wp = Client('http://127.0.0.1/wordpress/xmlrpc.php', 'admin', 'admin')
        #示例：wp = Client('http://www.python-cn.com/xmlrpc.php','username','password')
        post = WordPressPost()
        post.title = data['title']
        post.content = data['content']
        post.post_status = 'publish'
        #发送到WordPress
        wp.call(NewPost(post))
        # time.sleep(3)
        # print 'posts updates'
 
if __name__=='__main__':
    vr = Vr186()
    res = vr.get_mysql_data()
    print res
    print 'end'
