from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^center/$', views.Center, name="center"),
    url(r'^single/$', views.single, name="single"),

]