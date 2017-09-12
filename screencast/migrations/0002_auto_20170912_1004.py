# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 10:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('screencast', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='screencast',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='images%Y/%m/%d', verbose_name='Cover'),
        ),
        migrations.AlterField(
            model_name='screencast',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='screencast',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='screencast',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos%Y/%m/%d', verbose_name='Video'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Subject'),
        ),
    ]