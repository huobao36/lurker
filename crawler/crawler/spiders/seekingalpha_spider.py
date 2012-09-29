# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from crawler.items import ContentItem
from scrapy import log
from BeautifulSoup import BeautifulSoup
from scrapy.http import Request

class SeekingAlpahSpider(BaseSpider):
    name = "seekingalpha"
    allowed_domains = ["seekingalpha.com"]
    start_urls = [
    ]
    symbols = ['AAPL']
    max_visit_page = 10000 
    article_view = "http://seekingalpha.com/symbol/{0}/in-focus?page={1}"
    domain_url = "http://www.seekingalpha.com"
    minid = -1
    def __init__(self):
        for symbol in self.symbols:
            for i in range(0, self.max_visit_page):
                self.start_urls.append(self.article_view.format(symbol, i))
    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        articlelinks = hxs.select("//ul[@class='quote_list']/li/div[@class='content']/a/@href") 
        for articlelink in articlelinks:
            href = articlelink.extract()
            log.msg("article content href: " + href, level = log.DEBUG)
            if len(href):
               href = self.domain_url + href
               log.msg("href:" + href, level = log.DEBUG)
               yield Request(href, callback = self.parse_article_page)
    
    def parse_article_page(self, response):
        hxs = HtmlXPathSelector(response)
        header = hxs.select("//div[@id='page_header']/h1/span/text()")[0].extract()
        log.msg("article header:" + str(header), level = log.DEBUG)
        content_item = ContentItem()
        content_item['title'] = header
        paras = hxs.select("//div[@id='article_body']/p").extract()
        soup = BeautifulSoup('\n'.join(paras)) 
        content_item['content'] = ''.join(soup.findAll(text=True)).replace('"','\"')
        content_item['time'] = hxs.select("//div[@class='article_info_pos']/span/text()")[0].extract()
        content_item['user_name'] = hxs.select("//a[@class='author_info_name']/text()")[0].extract()
        content_item['type'] = 'content'
        yield content_item
    


