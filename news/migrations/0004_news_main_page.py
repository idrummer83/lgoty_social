# Generated by Django 3.1.2 on 2020-10-04 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20201004_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='main_page',
            field=models.BooleanField(default=False, verbose_name='Главная страница'),
        ),
    ]
