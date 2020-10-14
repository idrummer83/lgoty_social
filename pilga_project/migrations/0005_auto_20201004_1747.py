# Generated by Django 3.1.2 on 2020-10-04 14:47

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('pilga_project', '0004_auto_20201003_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='image',
            field=filer.fields.image.FilerImageField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='slider_images', to=settings.FILER_IMAGE_MODEL, verbose_name='Изображение'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='SliderImages',
        ),
    ]
