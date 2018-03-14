from django.db import models
#创建用户数据表
class User(models.Model):
    #性别
    GENDER_CHOICES = (
        ('男','男'),
        ('女','女')
    )
    name = models.CharField(max_length=30,unique=True)