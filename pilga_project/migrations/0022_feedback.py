# Generated by Django 3.1.2 on 2020-10-10 21:04

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilga_project', '0021_auto_20201010_2258'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Имя и Фамилия')),
                ('message', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Сообщение')),
                ('theme', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Тема сообщения')),
                ('phone', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Контактный телефон')),
                ('email', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
            },
        ),
    ]
