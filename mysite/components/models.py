from django.db import models
from django.urls import reverse


# Create your models here.

class Components(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='фото')
    description = models.TextField(max_length=1000, verbose_name='описание')
    tel = models.CharField(max_length=13, verbose_name='телефон')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    time_upgrate = models.DateTimeField(auto_now=True, verbose_name='последнее редактирование')
    is_publishes = models.BooleanField(default=True, verbose_name='статус пупликации')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Компьютерные комплектующие'
        verbose_name_plural = 'Компьютерные комплектующие'
        ordering = ['-time_create', 'name']


class Category(models.Model):
    type_comp = models.CharField(max_length=50, db_index=True, verbose_name='тип компонента')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.type_comp

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.id})

    class Meta:
        verbose_name = 'Категория компонента'
        verbose_name_plural = 'Категории компонентов'
        ordering = ['id']
