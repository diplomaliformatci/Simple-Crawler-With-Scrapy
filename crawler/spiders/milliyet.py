# -*- coding: utf-8 -*-
#! /usr/bin/python3
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import HtmlResponse
from scrapy.http import Request
class MilliyetSpider(scrapy.Spider):
    name = "milliyet"
    allowed_domains = ["milliyet.com"]
    start_urls = ['http://www.milliyet.com/erdogan-dan-flas-sozler-siyaset-2377341']


    def parse(self,response):
        if response.xpath('//h1//text()').extract():
            tag = response.xpath('//h1//text()').extract()
        elif response.xpath('//h2//text()').extract():
            tag = response.xpath('//h2//text()').extract()
        elif response.xpath('//h3//text()').extract():
            tag = response.xpath('//h3//text()').extract()
        elif response.xpath('//h4//text()').extract():
            tag = response.xpath('//h4//text()').extract()
        elif response.xpath('//h5//text()').extract():
            tag = response.xpath('//h5//text()').extract()
        elif response.xpath('//h6//text()').extract():
            tag = response.xpath('//h6//text()').extract()

        if response.xpath('//div[@class="date"]//text()').extract():
            date = response.xpath('//div[@class="date"]//text()').extract()

        parsed = response.xpath('//div/p//text()').extract()
        links  = ''.join(response.xpath('//a/@href').extract())
        for link in links:
            yield Request(link,callback=self.parse)
        parsed.encode('utf-8')
        for word in ''.join(parsed).split():
            yield {
                'word' : word,
                'url' : response.url,
                'date' : date,
                'tag' : tag
            }




        next_page_url = response.xpath(//a[])
        print('URL !!!!!!!!!!  ' + 'worddict !!!!!!!!!' + worddict.items() +  response.url + '\n\n\n\n\n\n')


