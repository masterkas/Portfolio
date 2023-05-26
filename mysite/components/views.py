from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from .forms import Add_postForm
from .models import Components, Category

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Контакты", 'url_name': 'contacts'},
    {'title': "Об авторе", 'url_name': 'about_me'},
    {'title': "Добавить объявление", 'url_name': 'add_post'},
    {'title': "Войти", 'url_name': 'login'},

]

class ComponentsHome(ListView):
    model = Components
    template_name = 'components/index.html'
    context_object_name = 'comp'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Components.objects.filter(is_publishes = True)





# def index(request):
#     comp = Components.objects.all()
#     # cats = Category.objects.all() заменил на тег
#
#     context = {
#         'comp': comp,
#         # 'cats': cats, заменил га тег
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0
#     }
#     return render(request, 'components/index.html', context=context)


class ComponentsCategory(ListView):
    model = Components
    template_name = 'components/index.html'
    context_object_name = 'comp'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория - ' + str(context['comp'][0].cat)
        context['cat_selected'] = context['comp'][0].cat_id
        return context

    def get_queryset(self):
        return Components.objects.filter(cat__slug=self.kwargs['cat_slug'], is_publishes = True)

# def show_category(request, cat_slug):
#     cat_id = Category.objects.get(slug=cat_slug).pk
#     comp = Components.objects.filter(cat_id=cat_id)
#     # cats = Category.objects.all() заменил га тег
#     if len(comp) == 0:
#         raise Http404()
#
#     context = {
#         'comp': comp,
#         # 'cats': cats, заменил га тег
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_id,
#     }
#     return render(request, 'components/index.html', context=context)


def about(request):
    return render(request, 'components/about.html', {'menu': menu, 'title': 'Обо мне'})

def contacts(request):
    return HttpResponse('Как со мной связаться')

def about_me(request):
    return HttpResponse('Обо мне')

def add_post(request):
    if request.method == "POST":
        form = Add_postForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            # try:
            #     Components.objects.create(**form.cleaned_data)
            # except:
            #     form.add_error(None, "Ошибка добавления объявления")
            form.save()
            return redirect('home')
    else:
        form = Add_postForm()
    return render(request, 'components/add_post.html', {'form': form, 'menu': menu, 'title': 'Добавление объявления'})

def login(request):
    return HttpResponse('Страница авторизации')


class ShowPost(DetailView):
    model = Components
    template_name = 'components/index.html'
    context_object_name = 'comp'
    allow_empty = False



# def show_post(request, post_slug):
#     post = get_object_or_404(Components, slug=post_slug)
#     context = {
#         'post': post,
#         # 'cats': cats, заменил на тег
#         'menu': menu,
#         'title': post.name,
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'components/post.html', context=context)





def pagenotfound(request, exception):
    return HttpResponseNotFound('<h1>СТРАНИЦА НЕ НАЙДЕНА</h1>')

