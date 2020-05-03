from . import views
from django.urls import path

app_name = 'farmzoneweb'

urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.index, name='about'),
]