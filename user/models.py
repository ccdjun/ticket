from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField('id',primary_key=True)
    user_name = models.CharField('用户名', max_length=10)
    password = models.CharField('用户密码', max_length=16)
    email = models.CharField('用户邮箱', max_length=30)
    user_status = models.IntegerField('用户状态', default=0) #0为普通用户 1为管理员用户