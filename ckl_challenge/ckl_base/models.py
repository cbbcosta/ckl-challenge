from django.db import models


class Outlet(models.Model):
    name = models.CharField(max_length=50, null=True)
    outlet_url = models.CharField(max_length=140)
    pub_date = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.name



class Author(models.Model):
    name = models.CharField(max_length=100, null=True)
    twitter_handle = models.CharField(max_length=50, null=True)
    profile_page = models.CharField(max_length=200)   
    
    def __str__(self):
        return self.name
    
    
    
class Article(models.Model):
    title = models.CharField(max_length=150, null=True)
    content = models.TextField()
    pub_date = models.DateTimeField(null=True, auto_now_add=True)
    authors = models.ManyToManyField('Author')
    tags = models.ManyToManyField('Tag')
    outlet = models.ForeignKey('Outlet', related_name='outlet_article')

    
    def __str__(self):
        return self.title


class Tag(models.Model):
    tag_description = models.CharField(max_length=100, null=True)
    tag_url = models.CharField(max_length=200, null=True)
    
    def __str_(self):
        return self.tag_description
        
    
    

