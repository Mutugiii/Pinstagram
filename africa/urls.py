from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
        path('', views.index, name='welcome'),
        path('search/', views.search, name='search'),
        path('locations/<str:region>', views.locations, name='locations'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)