from scrapy.spiders import SitemapSpider
from scrapy.selector import Selector    
from cklchallengescrapy.items import OutletItem

class NewsOutletSpider(SitemapSpider):
    name = "outlet-news-spider"
    allowed_domains = ["techcrunch.com"]
    sitemap_urls = ["https://techcrunch.com/news-sitemap.xml"]
#     sitemap_rules = [('/news-sitemap.xml', 'parse_news')]
    namespaces = {
        'news': 'http://www.google.com/schemas/sitemap-news/0.9',
    }
    
    def parse(self, response):
        Selector.register_namespace(self, 'news', "http://www.google.com/schemas/sitemap-news/0.9")
        
        outlet_url = response.url
        name = response.xpath('//title/text()').extract()[0:]
        pub_date = response.xpath('//publication_date/text()').extract()
    
        return OutletItem(outlet_url=outlet_url, name=name, pub_date=pub_date)