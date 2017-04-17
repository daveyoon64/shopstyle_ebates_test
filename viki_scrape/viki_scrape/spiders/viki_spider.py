import scrapy
from scrapy.http.request import Request
import json

url = 'http://api.viki.io/v4/videos.json?app=100250a&per_page=10&page=%d'


class VikiSpider(scrapy.Spider):
    name = "viki"
    start_urls = [url % 1]
    
    
    def __init__(self):
        self.page_number = 1
        self.true_flags = 0
        self.false_flags = 0

    def parse(self, response):
        json_res = json.loads(response.body_as_unicode())
        for key, value in json_res.items():
            if isinstance(value, list):
                for d in value:
                    if (d['flags']['hd'] == True):
                        self.true_flags += 1
                    elif (d['flags']['hd'] == False):
                        self.false_flags += 1
                    else:
                        continue
        self.log("True Flags: %d" % self.true_flags)
        self.log("False Flags: %d" % self.false_flags)

        if json_res['more'] == True:
            self.page_number += 1
            yield Request(url % self.page_number)