#coding: utf-8
from __future__ import absolute_import

from django.contrib import admin

from .models import Subject, Category, Screencast

class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ['subject', 'date']
    list_filter = ('subject', 'date',)
    search_fields = ('subject',)

    class Meta:
        model = Subject
admin.site.register(Subject, SubjectModelAdmin)

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['category', 'date']
    list_filter = ('category', 'date',)
    search_fields = ('category',)

    class Meta:
        model = Category
admin.site.register(Category, CategoryModelAdmin)

class ScreencastModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'categories', 'date']
    list_filter = ('title', 'categories', 'date',)
    search_fields = ('title', 'categories', 'date',)

    class Meta:
        model = Screencast
admin.site.register(Screencast, ScreencastModelAdmin)
