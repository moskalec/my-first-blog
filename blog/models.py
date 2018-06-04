from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=80)


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(height=100, width=100)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey('User', on_delete=models.CASCADE)


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(height=700, width=700)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(blank=True, null=True)
    publication_date = models.DateTimeField(blank=True, null=True)
    visible = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey('User', on_delete=models.CASCADE)


class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(blank=True, null=True)
    articles = models.ManyToManyField('Article')


class Comment(models.Model):
    content = models.CharField(max_length=1000)
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)


#
#class Post(models.Model):
#    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#    title = models.CharField(max_length=200)
#    text = models.TextField()
#    created_date = models.DateTimeField(
#            default=timezone.now)
#    published_date = models.DateTimeField(
#            blank=True, null=True)
#
#    def publish(self):
#        self.published_date = timezone.now()
#        self.save()
#
#    def __str__(self):
#        return self.title