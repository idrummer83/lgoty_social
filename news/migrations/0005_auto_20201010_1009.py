# Generated by Django 3.1.2 on 2020-10-10 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_main_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Создано'),
        ),
    ]
