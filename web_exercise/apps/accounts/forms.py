from django import forms
from django.forms import widgets
from .models import User
from django.core.exceptions import ValidationError
# 给check_password改个名字，叫auth_check_password,怕跟变量冲突
from django.contrib.auth.hashers import check_password as auth_check_password


# 注册表单
class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(label="密 码2",
                                widget=widgets.PasswordInput(attrs={
                                    "id": "passwd2",
                                    "class": "inputstyle2",
                                    "name": "password2",
                                }))
    mobile_captcha = forms.CharField(label="验证码", widget=widgets.TextInput(
        attrs={"class": "inputstyle2",
               "style": "width: 95px;",
               "error_messages": {"invalid": "验证码错误"},
               "name": "mobile_captcha",
               }))

    class Meta:
        model = User
        fields = ['username', 'mobile', 'password']
        widgets = {
            'username': widgets.TextInput(attrs={"class": "inputstyle2",
                                                 "id": "user",
                                                 "name": "username",
                                                 }),
            'mobile': widgets.TextInput(attrs={"class": "inputstyle2",
                                               "id": "mobile", "name": "mobile",
                                               }),
            'password': widgets.PasswordInput(attrs={"class": "inputstyle2",
                                                     "id": "passwd",
                                                     "name": "password",
                                                     }),
        }

    # username是否重复django会自动检查，因为它是unique的，所以不需要自己写clean_username

    def clean_mobile(self):
        ret = User.objects.filter(mobile=self.cleaned_data.get("mobile"))
        if not ret:
            return self.cleaned_data.get("mobile")
        else:
            raise ValidationError("手机号已绑定")

    def clean_password(self):
        data = self.cleaned_data.get("password")
        if not data.isdigit():
            return self.cleaned_data.get("password")
        else:
            raise ValidationError("密码不能全是数字")

    # clean跟其他clean_字段名不同，它不需要返回数据
    def clean(self):
        if self.cleaned_data.get("password") == self.cleaned_data.get("password2"):
            return self.cleaned_data
        else:
            raise ValidationError("两次密码不一致")

    def clean_username(self):
        # self.cleaned_data.get("username") =》获取表单提交的username数据
        users = User.objects.filter(username=self.cleaned_data.get("username"))
        if not users:
            return self.cleaned_data.get("username")
        else:
            raise ValidationError("该用户名已被使用")


# 登录表单
class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", max_length="24",
                               widget=widgets.TextInput(attrs={"class": "inputstyle",
                                                               "id": "u",
                                                               }))
    captcha = forms.CharField(label="验证码", widget=widgets.TextInput(
        attrs={"style": "width: 80px;",
               "class": "inputstyle",
               "id": "captcha",
               "onblur": "check_captcha()",
               "error_messages": {"invalid": "验证码错误"}}))
    password = forms.CharField(label="密 码",
                               widget=widgets.PasswordInput(attrs={"class": "inputstyle",
                                                                   "id": "p",
                                                                   }))

    def check_password(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        try:
            user = User.objects.get(username=username)
            return user, auth_check_password(password, user.password)
        except:
            return None, False

    def clean_username(self):
        # self.cleaned_data.get("username") =》获取表单提交的username数据
        ret = User.objects.filter(username=self.cleaned_data.get("username"))
        if ret:
            return self.cleaned_data.get("username")
        else:
            raise ValidationError("用户名或密码不正确")
