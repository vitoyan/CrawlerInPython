# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import logging

class WeatherPipeline(object):
    def __init__(self):
        self.file = open('ranks.json','wt')
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(str(item)+'\n')
        return item
