# Generated by Django 5.0.6 on 2024-05-21 13:27

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Страница'),
        ),
    ]
