import django
django.setup() 

from scrapy.spiders import SitemapSpider    
from cklchallengescrapy.items import OutletItem

class NewsOutletSpider(SitemapSpider):
    name = "outlet-news-spider"
    allowed_domains = ['techcrunch.com']
    sitemap_urls = ["https://techcrunch.com/news-sitemap.xml"]
#     sitemap_rules = [('/news-sitemap.xml', 'parse_news')]
    namespaces = {
        'news': 'http://www.google.com/schemas/sitemap-news/0.9',
    }
    
    def parse(self, response):
    
        outlet = OutletItem()
        outlet['outlet_url'] = response.url
        outlet['name'] = response.xpath('//news/title/text()').extract()
        outlet['pub_date'] = response.xpath('//news:news/news:publication_date/text()').extract()
    
        print (outlet)