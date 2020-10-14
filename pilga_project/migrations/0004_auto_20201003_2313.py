# Generated by Django 3.1.2 on 2020-10-03 20:13

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pilga_project', '0003_auto_20201003_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=2048, null=True, verbose_name='Текст для слайдера'),
        ),
        migrations.AddField(
            model_name='slider',
            name='description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=2048, null=True, verbose_name='Текст для слайдера'),
        ),
        migrations.AddField(
            model_name='slider',
            name='description_uk',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=2048, null=True, verbose_name='Текст для слайдера'),
        ),
    ]