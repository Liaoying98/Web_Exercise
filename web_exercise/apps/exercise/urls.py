from django.conf.urls import url
from . import views
urlpatterns = [
    # 首页
    url(r'^index/$', views.index.as_view(), name="index"),
    # 健身部位
    url(r'^index/(?P<id>\d+)/$', views.IndexDetail.as_view(), name="indexDetail"),
    # 部位
    url(r'^part/$', views.part, name="part"),

]