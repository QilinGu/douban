# -*- coding: utf-8 -*-
import scrapy

class DoubanItem(scrapy.Item):
    movie_name = scrapy.Field() #电影名称
    movie_star = scrapy.Field() #电影评分
    movie_url = scrapy.Field() #电影链接
