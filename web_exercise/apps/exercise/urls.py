from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    # 首页
    url(r'^index/$', views.index, name="index"),

]