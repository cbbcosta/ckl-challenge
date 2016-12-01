# -*- coding: utf-8 -*-
import django
from django.db.utils import IntegrityError
from scrapy.exceptions import DropItem

from ckl_base.models import Outlet, Article, Author
from cklchallengescrapy.items import AuthorItem, ArticleItem, OutletItem


django.setup()



# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
"""
Pipelines for storing scraped items in the database.
All the process_item methods are called for every pipeline component of each pipeline.
"""
class NewsOutletPipeline(object):
    def process_item(self, item, spider):
        outlet = Outlet(outlet_url=item['outlet_url'], name=item['name'])
        outlet.save()
        return item

# class ArticlePipeline(object):
#     def process_item(self, item, spider):
#         url = item['url']
#         outlet = Outlet.objects.get(outlet_url__exact=url)
#         article = Article(title=item['title'][0],
#                 pub_date=item['pub_date'], content=item['content'], outlet = outlet)
#         try:
#             article.save()
#         except IntegrityError:
#             raise DropItem("Contains duplicate domain: %s" % item['url'][0])
#         return item




# class AuthorPipeline(object):
#     def process_item(self, item, spider):
#         url = item['url']
#         article = Article.objects.get(url__exact=url)
#         author = Author(name=item['name'][0],
#                 profile_page=item['profile_page'])
#         article.authors=author
#         article.save()
#         if Author.objects.get(name__exact=author.name) is None:
#             author.save()
#         return item

# class OutletPipeline(object):
#     def process_item(self, item, spider):
#         """"Save outlets into the database."""
#         outlet = OutletItem(**item)
#         if outlet.django_model.objects.filter(name__exact=item.name).first() == None:
#             outlet.save()
#             return outlet
#         
# 
# class AuthorPipeline(object):
#     def process_item(self, item, spider):
#         """Save authors into the database."""                  
#         author = AuthorItem(**item)
#         if author.django_model.objects.get(name__exact=item.name):
#             return author
#         else:
#             author.save()
#             return author
# 
# class ArticlePipeline(object):
#     """Save the articles into the database. """
# 
#     def process_item(self, item, spider):
#         """Save deals in the database.
# 
#         """
#         article = ArticleItem(**item)
#         outlet = OutletItem.django_model.objects.get(outlet_url__exact=item.url)
#         article.save(commit=False)
#         article.django_model.outlet = outlet.id
#         article.save()
#                 
#     
#         return item
