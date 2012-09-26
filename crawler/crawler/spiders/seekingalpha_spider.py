from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from crawler.items import ContentItem
from scrapy import log
from scrapy.http import Request

class SeekingAlpahSpider(BaseSpider):
    name = "seekingalpha"
    allowed_domains = ["seekingalpha"]
    start_urls = [
    ]
    symbols = ['AAPL']
    max_visit_page = 10
    article_view = "http://seekingalpha.com/symbol/{0}/in-focus?page={1}"

    def __init__(self):
        for symbol in self.symbols:
            for i in range(0, self.max_visit_page):
                self.start_urls.append(self.article_view.format(symbol, i))
             
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        articles = hxs.select("//ul[@class='quote_list']/li")
        log.msg("articles html ele" + str(articles) + '\n', level = log.DEBUG)
        for article in articles:
            log.msg("article content ele" + str(article.select("//div[@class='content']")) + '\n', level = log.DEBUG)
            href = article.select("//div[@class='content']/a/@href").extract()
            log.msg("article content href" + str(href) + '\n', level = log.DEBUG)
            if not href and len(href) > 0:
                yield Request(href[0], callback = self.parse_article_page)
   
    def extract_content(content):
        rawcontent = []
        paras = content.select("/p")
        for para in paras:
            rawcontent.append(para.extract())
        return ''.join(rawcontent)

    def parse_article_page(self, response):
        hxs = HtmlXPathSelector(response)
        header = hxs.select("//div[@class='page_header']/h1/span").extract()
        content_item = ContentItem()
        content_item['title'] = header
        body = hxs.select("//div[@id='article_body']")
        content_item['content'] = extract_content(body)
        content_item['time'] = hxs.select("//div[@class='article_info_pos']").extract()
        content_item['user_name'] = hxs.select("//a[@class='author_info_name']").extract()
        yield content_item


