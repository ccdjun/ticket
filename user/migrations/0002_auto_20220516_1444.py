# Generated by Django 2.1.15 on 2022-05-16 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=30, verbose_name='用户邮箱'),
        ),
    ]
