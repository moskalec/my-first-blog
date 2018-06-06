from django.urls import path
from . import views


urlpatterns = [
    path('', views.article_list, name='article_lists'),
    path('articles/', views.article_list, name='article_list'),
    path('article/new/', views.article_new, name='article_new'),
    # path('article/(?<pk>\d+)/', views.article_detail, name='article_detail',),
    # path('article/(?P<pk>\d+)/edit/', views.article_edit, name='article_edit'),
]

#Urls
#    /
#    /categories/
#    /categories/<category_title>/
#    /categories/<category_title>/articles/
#    /categories/<category_title>/articles/<article_title>/
#    /tags/
#    /tags/<tag_title>/
#
#    Requirements:
#    1. HRU only
#    2. Transliterated urls
#        e.g.:
#            category.title = 'спорт'
#            article.title = 'Финал Лиги Чемпионов все'
#
#            url => /categories/sport/articles/final-ligi-chempionov-vse/