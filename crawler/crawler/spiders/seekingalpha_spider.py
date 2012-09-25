from scrapy.spider import BaseSpider
import scrapy.selector.HtmlXPathSelector
import items
class SeekingAlpahSpider(BaseSpider):
    name = "seekingalpha"
    allowed_domains = ["seekingalpha"]
    article_view = 'http://seekingalpha.com/symbol/%s/in-focus?page=%s'  
    start_urls = [
    ]
    max_visit_page = 10
    def __init__(self, symbols)
        for symbol in symbols:
            for i in range(0, max_visit_page):
                start_urls.append(symbolpage.format(article_view, symbol, i))
             
    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        articles = hxs.select('//ul/li[@class=quote_list]')
        for article in articles:
            href = article.select('/content/a/href/').extract()
            yield(href, parse_article_page)
   
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
        yield(content_item)

