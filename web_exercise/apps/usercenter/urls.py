from django.conf.urls import url, include
from . import views

urlpatterns = [
    # 个人资料
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    # 修改密码
    url(r'^change_passwd/$', views.ChangePasswdView.as_view(), name='change_passwd'),

]