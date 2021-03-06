# Generated by Django 3.1.2 on 2020-10-10 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20201010_2158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='news',
            new_name='tags',
        ),
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.CharField(max_length=500, null=True, verbose_name='Автор новости'),
        ),
        migrations.AddField(
            model_name='news',
            name='author_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Автор новости'),
        ),
        migrations.AddField(
            model_name='news',
            name='author_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Автор новости'),
        ),
        migrations.AddField(
            model_name='news',
            name='author_uk',
            field=models.CharField(max_length=500, null=True, verbose_name='Автор новости'),
        ),
    ]
