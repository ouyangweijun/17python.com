# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-14 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20171202_0227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=20, verbose_name='图片标题')),
                ('path', models.ImageField(default='upload/default.jpg', upload_to='upload/%Y/%m', verbose_name='图片')),
            ],
            options={
                'verbose_name': '网站相册',
                'verbose_name_plural': '网站相册',
            },
        ),
    ]