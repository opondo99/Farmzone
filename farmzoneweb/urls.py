from django.urls import path

from . import views

app_name = 'farmzoneweb'

urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.index, name='about'),
]
