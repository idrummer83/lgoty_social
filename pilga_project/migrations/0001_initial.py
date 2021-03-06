# Generated by Django 3.1.2 on 2020-10-02 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='slider_image', to=settings.FILER_IMAGE_MODEL, verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Изображения слайдера',
                'verbose_name_plural': 'Изображения слайдера',
            },
        ),
    ]
