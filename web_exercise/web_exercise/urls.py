"""web_exercise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from .settings import MEDIA_ROOT
from . import views

urlpatterns = [
    # admin用户
    url(r'^admin/', admin.site.urls),
    # media 处理路由
    url(r'^media/(?P<path>.*)$',  serve, {"document_root": MEDIA_ROOT}),
    # ckeditor
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # 首页
    url(r'^exercise/', include('apps.exercise.urls', namespace="exercise")),
    url(r'^accounts/', include('apps.accounts.urls', namespace="accounts")),
    url(r'^apis/', include('apps.apis.urls', namespace="apis")),
    url(r'^slimming/', include('apps.slimming.urls', namespace="slimming")),
    url(r'^schedule/', include('apps.schedule.urls', namespace="schedule")),
    url(r'^equipments/', include('apps.equipments.urls', namespace="equipments")),
    url(r'^diet/', include('apps.diet.urls', namespace="diet")),
    url(r'^uc/', include('apps.usercenter.urls', namespace="uc")),
]
