from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/(?<pk>\d+)/', views.post_detail, name='post_detail',),
    path('post/new/', views.post_new, name='post_new'),
    path('post/(?P<pk>\d+)/edit/', views.post_edit, name='post_edit'),
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
#            articler.title = 'Финал Лиги Чемпионов все'
#
#            url => /categories/sport/articles/final-ligi-chempionov-vse/