menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Контакты", 'url_name': 'contacts'},
    {'title': "Об авторе", 'url_name': 'about_me'},
    {'title': "Добавить объявление", 'url_name': 'add_post'},
    {'title': "Войти", 'url_name': 'login'},

]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context