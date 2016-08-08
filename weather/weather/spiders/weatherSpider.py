import scrapy
import logging

from weather.items import WeatherItem

class WeatherSpider(scrapy.Spider):
    name = 'weather'
    allowed_domains = ['weather.com.cn']
    start_urls = ["http://www.weather.com.cn"]

    def parse(self, response):
        ranks = response.css('.rank')
        itemIndex = ['order','city','provenci','higestTempAndTime','tmpDiff','water']
        infoIndex = ['.ord','.city','.prov','.wd::text']
        elements = ['./i/text()','./a/text()','./a/text()']
        for rankClass in range(1, 4):
            rank = ranks.xpath('(./ul)[' + str(rankClass) + ']')
            for order in range(2, 8):
                infos  =  rank.xpath('(./li)[' + str(order) + ']')
                item = WeatherItem()
                for index in range(4):
                    index2 = index if index < 3  else index + rankClass - 1
                    record = infos.css(infoIndex[index])
                    record = record.xpath(elements[index]).extract() if index <3 else record.extract()
                    item[itemIndex[index2]]=record
                self.logger.info("%s",item)
                yield item
