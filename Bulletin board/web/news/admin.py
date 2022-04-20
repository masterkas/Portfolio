from django.contrib import admin
from .models import Articles
from .models import Author


admin.site.register(Articles)
admin.site.register(Author)

