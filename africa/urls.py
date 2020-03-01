from django.urls import path, re_path
from . import views

urlpatterns = [
        path('', views.index, name='welcome'),
        path('search/', views.search, name='search'),
]
