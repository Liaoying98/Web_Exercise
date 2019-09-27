from django.core.exceptions import ValidationError


# 选择部位验证器
def valid_difficulty(n):
    if n > 6 or n <1:
        raise ValidationError("部位选择介于1到6之间")