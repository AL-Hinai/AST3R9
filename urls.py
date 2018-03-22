from django.conf.urls import url
from AST3R9 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]