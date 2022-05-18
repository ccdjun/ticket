from django.db import models

# Create your models here.
class Ticket(models.Model):
    id = models.AutoField('id',primary_key=True)
    source = models.CharField('出发地', max_length=10)
    target = models.CharField('目的地', max_length=10)
    num = models.IntegerField('余票数量', max_length=20)
    begin = models.CharField('出发时间',max_length=20,null=True)
    end = models.CharField('到达时间',max_length=20, null=True)


class Order(models.Model):
    id = models.AutoField('id',primary_key=True) #订单id
    ticket_id = models.IntegerField('绑定的车票id', max_length=10)
    user_id = models.IntegerField('绑定的用户id', max_length=10)
    source = models.CharField('出发地', max_length=10)
    target = models.CharField('目的地', max_length=10)
    order_status = models.IntegerField('订单状态', default=0) #1为已抢到 0为未抢到
