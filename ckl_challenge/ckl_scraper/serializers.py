from rest_framework import serializers

from ckl_scraper.models import Outlet, Author, Article, Tag


class OutletSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Outlet
        fields = '__all__'
        

class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = '__all__'
        

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'
        

class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = '__all__'