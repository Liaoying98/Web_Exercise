from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    # 登录,注册
    url(r'^login/$', views.Login.as_view(), name="login"),
    # 退出
    url(r'^logout/$', views.Logout, name="logout"),
    # 忘记密码
    url(r'password/forget/$', views.PasswordForget.as_view(), name="password_forget"),
    # 重置密码
    url(r'password/reset/(\w+)/$', views.PasswordReset.as_view(), name="password_reset"),

]
