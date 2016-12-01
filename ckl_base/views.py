from django.shortcuts import render
from django.db.models import F
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView

from ckl_base.models import Outlet, Author, Article, Tag
from ckl_base.serializers import OutletSerializer, AuthorSerializer, \
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
    

class ArticleSearch(APIView):
    
    def post(self, request, format=None):
        article_title = None
        try:
            article_title = request.query_params['title']
        except:
            return Response(status=HTTP_404_NOT_FOUND)
        
        articles = Article.objects.filter(F(title__icontains=article_title))
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
        
    


class TagList(generics.ListAPIView):
    """
    Return all the tags in the database.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
    
class TagDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Return an specific tag, passing the id, and also update and delete the selected tag.
    """
    
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
