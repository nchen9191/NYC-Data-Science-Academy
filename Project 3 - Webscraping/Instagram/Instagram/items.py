# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

###### Scrapy class that contains each item #######
class InstagramItem(scrapy.Item):
    image_urls = scrapy.Field()
    numLikes = scrapy.Field()
    numComments = scrapy.Field()
    location = scrapy.Field()

