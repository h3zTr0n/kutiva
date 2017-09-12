from django.db import models
from django.forms import ModelForm
from django.utils import timezone

from django.utils.translation import ugettext_lazy as _

class Subject(models.Model):
    subject = models.CharField(_("Subject"), max_length=100)
    date = models.DateField(_("Date"), default=timezone.now)

    class Meta:
        ordering = ['-date']
        verbose_name = "SUBJECT"
        verbose_name_plural = "SUBJECTS"

    def __str__(self):
        return self.subject


class Category(models.Model):
    category = models.CharField(_("Category"), max_length=100)
    date = models.DateField(_("Date"), default=timezone.now)

    class Meta:
        ordering = ['-date']
        verbose_name = "CATEGORY"
        verbose_name_plural = "CATEGORIES"

    def __str__(self):
        return self.category


class Screencast(models.Model):
    title = models.CharField(_("Title"), max_length=300)
    description = models.TextField(_("Description"), blank=True, null=True)
    subjects = models.ManyToManyField(Subject)
    categories = models.ForeignKey(Category)
    cover = models.ImageField(_("Cover"), upload_to='images%Y/%m/%d')
    video = models.FileField(_("Video"), upload_to='videos%Y/%m/%d')
    date = models.DateField(_("Date"), default=timezone.now)
    """docstring for Lesson"""

    class Meta:
        ordering = ['-date']
        verbose_name = "SCREENCAST"
        verbose_name_plural = "SCREENCASTS"

    def __str__(self):
        return self.title


# # Create your models here.
