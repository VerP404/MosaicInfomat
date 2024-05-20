# Generated by Django 5.0.6 on 2024-05-20 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/')),
            ],
        ),
    ]
