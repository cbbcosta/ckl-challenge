# -*- coding: utf-8 -*-
import django

from ckl_base.models import Outlet
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
class ArticleTestPipeline(object):
    def process_item(self, item, spider):
        item.save(commit=False)
        url = item['url'] 
        item['outlet_id'] = Outlet.objects.get(id=1).id
        item.save()
        return item

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
