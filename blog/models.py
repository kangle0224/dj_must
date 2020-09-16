from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    name = models.CharField('名称', max_length=50)
    status = models.PositiveIntegerField('状态', default=STATUS_NORMAL, choices=STATUS_ITEMS)
    is_nav = models.BooleanField('是否为导航', default=False)
    owner = models.ForeignKey('作者', User)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = '分类'
