from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    data = {'title': 'Добро пожаловать на доску объявлений'}

    return render(request, "app/index.html", data)


def about(request):
    return render(request, "app/about.html")
