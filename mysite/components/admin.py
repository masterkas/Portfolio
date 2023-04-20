from django.contrib import admin
from .models import *
# Register your models here.


class ComponentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cat', 'time_create', 'photo', 'is_publishes')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'description')
    list_editable = ('is_publishes',)
    list_filter = ('is_publishes', 'time_create')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_comp')
    list_display_links = ('id', 'type_comp')
    search_fields = ('type_comp',)

admin.site.register(Components, ComponentsAdmin)
admin.site.register(Category, CategoryAdmin)