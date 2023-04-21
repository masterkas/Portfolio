from django.conf.urls.static import static
from django.urls import path

from mysite import settings
from .views import *

urlpatterns = [
    path('', index, name='home'),

    path('about/', about, name='about'),
    path('about_me/', about_me, name='about_me'),
    path('add_post/', add_post, name='add_post'),
    path('contacts/', contacts, name='contacts'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:cat_id>/', show_category, name='category'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)