from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from .models import Components, Category

menu = [

    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Контакты", 'url_name': 'contacts'},
    {'title': "Об авторе", 'url_name': 'about_me'},
    {'title': "Добавить объявление", 'url_name': 'add_post'},
    {'title': "Войти", 'url_name': 'login'},

]


def index(request):
    comp = Components.objects.all()
    # cats = Category.objects.all() заменил га тег

    context = {
        'comp': comp,
        # 'cats': cats, заменил га тег
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0
    }
    return render(request, 'components/index.html', context=context)


def about(request):
    return render(request, 'components/about.html', {'menu': menu, 'title': 'Обо мне'})

def contacts(request):
    return HttpResponse('Как со мной связаться')

def about_me(request):
    return HttpResponse('Обо мне')

def add_post(request):
    return HttpResponse('Добавить объявление')

def login(request):
    return HttpResponse('Страница авторизации')


def show_post(request, post_slug):
    post = get_object_or_404(Components, slug=post_slug)
    context = {
        'post': post,
        # 'cats': cats, заменил га тег
        'menu': menu,
        'title': post.name,
        'cat_selected': post.cat_id,
    }
    return render(request, 'components/post.html', context=context)


def show_category(request, cat_id):
    comp = Components.objects.filter(cat_id=cat_id)
    # cats = Category.objects.all() заменил га тег
    if len(comp) == 0:
        raise Http404()

    context = {
        'comp': comp,
        # 'cats': cats, заменил га тег
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id
    }
    return render(request, 'components/index.html', context=context)


def pagenotfound(request, exception):
    return HttpResponseNotFound('<h1>СТРАНИЦА НЕ НАЙДЕНА</h1>')

