from django.db import models


class Articles(models.Model):
    POST_TYPES = [('b', 'куплю'), ('s', 'продам'), ('r', 'обменяю')]
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    image = models.ImageField('Фото', upload_to='photo/%Y/%m/%d')
    full_text = models.TextField('Текст объявления')
    date = models.DateTimeField('Дата публикации')
    post_type = models.CharField(max_length=1, choices=POST_TYPES)
    name = models.CharField('Имя', max_length=200)
    email = models.EmailField('Email')
    tel = models.CharField('Телефон', max_length=50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Author(models.Model):
    name = models.CharField(max_length=60)
