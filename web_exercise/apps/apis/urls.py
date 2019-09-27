from django.conf.urls import url, include
from . import views

urlpatterns = [
    # 获取手机验证码
    url(r'^mobile_captcha/$', views.get_mobile_captcha, name='get_mobile_captcha'),
    # 获取图片验证码
    url(r'^get_captcha/$', views.get_captcha, name='get_captcha'),
    # 验证图片验证码
    url(r'^check_captcha/$', views.check_captcha, name='check_captcha'),
    # 上传头像
    url(r'^change_avator/$', views.ChangeAvator.as_view(), name='change_avator'),

]