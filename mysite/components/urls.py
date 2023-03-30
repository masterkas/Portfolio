from django.conf.urls.static import static
from django.urls import path

from mysite import settings
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('categories/', categories),
    path('categories/<int:cat_id>/', categories_id),
    path('about/', about, name='about'),
    path('add_post/', add_post, name='add_post'),
    path('contacts/', contacts, name='contacts'),
    path('login/', login, name='login'),
    path('post/<slug:post_id>/', show_post, name='post'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)