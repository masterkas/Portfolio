from django.db import models
from django.urls import reverse


# Create your models here.

class Components(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(max_length=1000)
    tel = models.CharField(max_length=10)
    time_create = models.DateTimeField(auto_now_add=True)
    time_upgrate = models.DateTimeField(auto_now=True)
    is_publishes = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id':self.pk})


class Category(models.Model):
    type_comp=models.CharField(max_length=50, db_index=True)
    def __str__(self):
        return self.type_comp

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id':self.pk})

