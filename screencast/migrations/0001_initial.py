# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 09:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, verbose_name='Category')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'CATEGORY',
                'verbose_name_plural': 'CATEGORIES',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Screencast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('cover', models.ImageField(upload_to='images%Y/%m/%d', verbose_name='Cover')),
                ('video', models.FileField(upload_to='videos%Y/%m/%d', verbose_name='Video')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='screencast.Category')),
            ],
            options={
                'verbose_name': 'SCREENCAST',
                'verbose_name_plural': 'SCREENCASTS',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, verbose_name='Subject')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'SUBJECT',
                'verbose_name_plural': 'SUBJECTS',
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='screencast',
            name='subjects',
            field=models.ManyToManyField(to='screencast.Subject'),
        ),
    ]