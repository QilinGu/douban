# -*- coding: utf-8 -*-

import MySQLdb

class DoubanPipeline(object):
    def process_item(self, item, spider):
    	print item
    	print  u'数据库写入准备...'
    	con = MySQLdb.connect('localhost','root','*********','douban',charset='utf8')
    	cur = con.cursor()
    	cur.execute('set names "utf8"')
    	sql = "insert into movies(name,points,url) values(%s,%s,%s)"
    	lis = (item['movie_name'],item['movie_star'],item['movie_url'])
    	try:

    		cur.execute(sql,lis)
    	except Exception,e:
    		print "insert Error...",e
    		con.rollback()
    	else:
    		con.commit()
    	cur.close()
    	con.close()

    	return item
        
