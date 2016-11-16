from django.conf.urls import url

from ckl_challenge.ckl_base import views


urlpatterns = [ 
    
    #Outlets
    url('^outlet/$', views.OutletListCreate.as_view(), name='outlets'),
    url('^outlet/(?P<pk>[0-9]+)/$', views.OutletDetails.as_view(), name='outlet-details'),
    
    #Authors
    url('^author/$', views.AuthorListCreate.as_view(), name='authors'),
    url('^author/(?P<pk>[0-9]+)/$', views.AuthorDetails.as_view(), name='author-details'),
#     url('^author/search/$', views.AuthorSearch.as_view(), name='author-search'),
    
    #Articles
    url('^article/$', views.ArticleListCreate.as_view(), name='article'),
    url('^article/(?P<pk>[0-9]+)/$', views.ArticleDetails.as_view(), name='article-details'),
    url('^article/search/$', views.ArticleSearch.as_view(), name='author-search'),
    
]