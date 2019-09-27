from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ..accounts.models import User
from .validator import valid_difficulty
# Create your models here.


class Category(models.Model):
    """分类"""
    name = models.CharField("分类名称", max_length=64)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):
    """标签"""
    name = models.CharField("标签名", max_length=64)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name}"


class Actions(models.Model):
    """健身部位"""
    DIF_CHOICES = (
        (1, "肩膀"),
        (2, "手臂"),
        (3, "胸部"),
        (4, "背部"),
        (5, "腰部"),
        (6, "腿部"),
    )
    select = models.IntegerField("部位选择", choices=DIF_CHOICES, validators=[valid_difficulty], null=True)
    category = models.ForeignKey(Category, verbose_name="所属分类", null=True)
    title = models.CharField("标题", unique=True, max_length=256)
    # 富文本编辑器RichTextUploadingField
    content = RichTextUploadingField("详情", null=True)
    contributor = models.ForeignKey(User, verbose_name="贡献者", null=True)
    pub_time = models.DateTimeField("入库时间", auto_now_add=True, null=True)
    # 审核状态
    status = models.BooleanField("审核状态", default=False)
    # 标签
    tag = models.ManyToManyField(Tag, verbose_name="部位标签")

    class Meta:
        verbose_name = "健身部位"
        verbose_name_plural = verbose_name
        # 设置权限
        permissions = (
                        ('can_change_question', "可以修改题目信息"),
                        ('can_add_question', "可以添加题目信息"),
                        ('can_change_question_status', '可以修改题目状态'),
                       )

    def __str__(self):
        return f"{self.id}:{self.title}"


class Part(models.Model):

    title = models.CharField("标题", unique=True, max_length=256)
    pic = models.ImageField("图片")

    class Meta:
        verbose_name = "身体部位"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.title}"

