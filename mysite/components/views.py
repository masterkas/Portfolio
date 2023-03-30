from django.http import HttpResponse
from django.shortcuts import render
from .models import *

menu = [
    {'title': "Главная страница", 'url_name': 'home'},
    {'title': "Обо мне", 'url_name': 'about'},
    {'title': "Добавить объявление", 'url_name': 'add_post'},
    {'title': "Контакты", 'url_name': 'contacts'},
    {'title': "Войти", 'url_name': 'login'},

]


def index(request):
    comp = Components.objects.all()
    context = {
        'comp': comp,
        'menu': menu,
        'title': 'Главная страница'

    }
    return render(request, 'components/index.html', context=context)


def about(request):
    return render(request, 'components/about.html', {'menu': menu, 'title': 'Обо мне'})

def add_post(request):
    return HttpResponse('Добавить объявление')

def contacts(request):
    return HttpResponse('Как со мной связаться')

def login(request):
    return HttpResponse('Страница авторизации')


def show_post(request, post_id):
    return HttpResponse(f'Страница объявления {post_id}')





def categories(request):
    return HttpResponse('<h1>Привет! Здесь можно выбрать категорию товара</h1>')


def categories_id(request, cat_id):
    return HttpResponse(f'<h1>Привет! Вы находитесь в категории {cat_id}</h1>')
