# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import logging


class SmzdmPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host='localhost', user='root', passwd='mysql900127', db='test_python', charset="utf8")

    def process_item(self, item, spider):
        sql_select = "SELECT id FROM smzdm WHERE article_id =  '%s'" % item['article_id']
        try:
            self.cursor.execute(sql_select)
            result = self.cursor.fetchall()
            if(len(result) == 0):
                sql_insert = "INSERT INTO smzdm (article_id,article_url,title,price,source,submit_time)" + \
                        " VALUES ('%s','%s','%s','%s','%s',from_unixtime(%d))" % \
                        (item['article_id'], item['article_url'], item['title'], item['price'], item['source'], int(item['time']))
                self.cursor.execute(sql_insert)
                self.conn.commit()
                # print 'Insert article: %s' % item['article_id']
            else:
                # print 'Repeat article'
                pass
        except:
            logging.error(str(item))
            print "Error: unable to fecth data"
        return item

    def open_spider(self, spider):
        self.cursor = self.conn.cursor()
        print '++++++++++++++++++++++++++++++++++++++++++++'

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
        print '----------------------------------------------'
