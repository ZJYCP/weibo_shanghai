# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mblogid=scrapy.Field()  #微博id
    created_at=scrapy.Field()  #发布时间
    content=scrapy.Field()  #发布文字内容
    pic_count=scrapy.Field()  #发布图片数量
    username=scrapy.Field()  #用户名
    gender=scrapy.Field()  #用户性别
    followers_count=scrapy.Field()  #粉丝数
    friends_count=scrapy.Field()  #关注数
    statuses_count=scrapy.Field()  #微博数
    user_created_at=scrapy.Field()  #注册时间
    location=scrapy.Field()  #定位地点
    
