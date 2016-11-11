from django.shortcuts import render
from rest_framework import generics

from ckl_scraper.models import Outlet, Author, Article, Tag
from ckl_scraper.serializers import OutletSerializer, AuthorSerializer, \
    ArticleSerializer, TagSerializer


class OutletListCreate(generics.ListCreateAPIView): 
    """
    Return all the outlets and allow creating a new outlet
    """
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer
    


class OutletDetails(generics.RetrieveUpdateAPIView):   
    """
    Return an specific outlet, passing the id, and also update and delete the selected outlet.
    """
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer
    


class AuthorListCreate(generics.ListCreateAPIView):  
    """
    Return all the authors and allow creating a new author
    """   
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer 



class AuthorDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Return an specific author, passing the id, and also update and delete the selected author.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class ArticleListCreate(generics.ListCreateAPIView):
    """
    Return all the articles and allow creating a new article.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer



class ArticleDetails(generics.RetrieveUpdateDestroyAPIView): 
    """
    Return an specific article, passing the id, and also update and delete the selected article.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    


class TagList(generics.ListAPIView):
    
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
    
class TagDetails(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
