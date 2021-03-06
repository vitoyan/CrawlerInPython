# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    order = scrapy.Field()
    city = scrapy.Field()
    provenci = scrapy.Field()
    higestTempAndTime = scrapy.Field()
    tmpDiff = scrapy.Field()
    water = scrapy.Field()
