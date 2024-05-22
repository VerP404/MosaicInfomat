from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Block(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


class Button(models.Model):
    label = models.CharField(max_length=200)
    link = models.URLField(blank=True, null=True)
    page = models.ForeignKey('Page', on_delete=models.SET_NULL, null=True, blank=True)
    block = models.ForeignKey(Block, related_name='buttons', on_delete=models.CASCADE)

    def __str__(self):
        return self.label


class Page(models.Model):
    title = models.CharField(max_length=200)
    content = CKEditor5Field(verbose_name='Страница', config_name='extends')

    def __str__(self):
        return self.title


class Settings(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return f"Header: {self.title or 'No Title'}"
