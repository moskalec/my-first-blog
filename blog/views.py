from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import User, Category, Article, Tag, Comment
from .forms import ArticleForm


def article_list(request):
    articles = Article.objects.filter(publication_date__lte=timezone.now()).order_by('publication_date')
    return render(request, 'blog/article_list.html', {'articles': articles})


# Article.objects.get(pk=pk)


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article_detail.html', {'article': article})


def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.publication_date = timezone.now()
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'article_edit.html', {'form': form})


def article_edit(request, pk):
    post = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=post)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.publication_date = timezone.now()
            article.save()
            return redirect('article_detail', pk=post.pk)
    else:
        form = ArticleForm(instance=post)
    return render(request, 'blog/article_edit.html', {'form': form})

