# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-05 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0008_portfolio_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=40)),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('job_title', models.CharField(max_length=40)),
                ('department', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
            ],
        ),
    ]