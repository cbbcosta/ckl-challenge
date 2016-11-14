# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import django
django.setup()

#Import DjangoItem to use django project models.
from scrapy.item import Field
from scrapy_djangoitem import DjangoItem
from ckl_base.models import Outlet, Author, Article, Tag


class OutletItem(DjangoItem):
    django_model = Outlet   

class AuthorItem(DjangoItem):
    django_model = Author
    
class ArticleItem(DjangoItem):
    django_model = Article
    url = Field()
    
class TagItem(DjangoItem):
    django_model = Tag