from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView


def news_home(request):
    news = Articles.objects.all()
    return render(request, "news/news_home.html", {'news': news})


class News(DetailView):
    model = Articles
    template_name = 'news/news_one.html'
    context_object_name = 'article'


class NewsEditing(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


def create(request):

    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_home')

    else:
        form = ArticlesForm()
    data = {'form': form}
    return render(request, "news/create.html", data)
