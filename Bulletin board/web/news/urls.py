from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.news_home, name="news_home"),
    path('create', views.create, name="create"),
    path('<int:pk>', views.News.as_view(), name='news_one'),
    path('<int:pk>/editing', views.NewsEditing.as_view(), name='news_editing'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)