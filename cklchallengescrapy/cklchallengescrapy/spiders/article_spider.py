from scrapy import Request
from scrapy.spider import Spider
from scrapy.spiders import BaseSpider

from cklchallengescrapy.items import ArticleItem, TagItem, AuthorItem


class ArticleTestSpider(BaseSpider):
    name="article_spider"
    allowed_domains=["techcrunch.com"]
    start_urls=["https://techcrunch.com/2016/11/13/how-drones-will-reshape-the-enterprise/"]
    
    def parse(self, response):
        for sel in response.xpath('//header[@class="article-header page-title"]'):
            title = sel.xpath('//h1/text()').extract()
            pub_date = sel.xpath('//div/div/time[@class="timestamp"]/@datetime').extract()
            content = sel.xpath('//div[@class="article-entry text"]/p/text()').extract()
            url = response.url
            return ArticleItem(title=title, pub_date=pub_date, content=content, url=url)
            


# class ArticleSpider(Spider):
#     name="article-spider"
#     allowed_domains=["techcrunch.com"]
#     start_urls=["https://techcrunch.com/2016/11/13/how-drones-will-reshape-the-enterprise/"]
#     
#     def parse(self, response):
#         for sel in response.xpath('//header[@class="article-header page-title"]'):
#             article = ArticleItem()
#             article['title'] = sel.xpath('//h1/text()').extract()
#             article['pub_date'] = sel.xpath('//div/div/time[@class="timestamp"]/@datetime').extract()
#             article['content'] = sel.xpath('//div[@class="article-entry text"]/p/text()').extract()
#             article['url'] = response.url
#                             
#             
#             print (article)
#             yield Request(str(self.start_urls), callback=self.parse_authors)
#             
#     def parse_authors(self, response):
#         for sel in response.xpath('//header[@class="article-header page-title"]'):
#             author = AuthorItem()
#             author['name'] = sel.xpath('.//div/div/a[@rel="author"]/text()').extract()
#             author['profile_page'] = "https://techcrunch.com" + str(sel.xpath('.//div/div/a[@rel="author"]/@href').extract())
#             
#             print (author)
#             yield Request(str(self.start_urls), callback=self.parse_tags)
#             
#     def parse_tags(self, response):
#         for sel in response.xpath('//div[@class="accordion recirc-accordion"]/ul/'):
#             for tag in sel.xpath('.//li/div[@class="loader acc-handle"]/a'):
#                 tag = TagItem()
#                 tag['tag_description'] = tag.xpath('.//text()').extract()
#                 tag['tag_url'] = tag.xpath('.//@href').extract()
#                 print (tag)
#             
