from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'description', 'content', 'image', 'created', 'updated', 'publication_date', 'visible', 'category', 'author')
