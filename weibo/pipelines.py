# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import logging
import datetime
from weibo import settings
LOG_FORMAT = "%(asctime)s-----------------%(levelname)s--------------------%(message)s"
logging.basicConfig(filename="log.log",level=logging.ERROR,format=LOG_FORMAT)
class WeiboPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host = settings.MYSQL_HOST,
            db = settings.MYSQL_DBNAME,
            user = settings.MYSQL_USER,
            passwd = settings.MYSQL_PASSWD,
            charset = 'utf8mb4',
            use_unicode = True
        )
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        try:
            self.cursor.execute("insert into OriginData (mblogid,publish_at,content,username,pic_count,gender,followers_count,friends_count,statuses_count,user_created_at,place,created_at) value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(item['mblogid'],item['created_at'],item['content'],item['username'],item['pic_count'],item['gender'],item['followers_count'],item['friends_count'],item['statuses_count'],item['user_created_at'],item['location'],datetime.datetime.now()))
            self.connect.commit()
        except Exception as error:
            logging.error(error)
        return item
    def close_spider(self,spider):
        self.connect.close();
