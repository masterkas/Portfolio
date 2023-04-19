from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
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
    cats = Category.objects.all()

    context = {
        'comp': comp,
        'cats': cats,
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


def show_post(request, post_id):
    return HttpResponse(f'Страница объявления {post_id}')


def show_category(request, cat_id):
    comp = Components.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    if len(comp) == 0:
        raise Http404()

    context = {
        'comp': comp,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id
    }
    return render(request, 'components/index.html', context=context)


def pagenotfound(request, exception):
    return HttpResponseNotFound('<h1>СТРАНИЦА НЕ НАЙДЕНА</h1>')

