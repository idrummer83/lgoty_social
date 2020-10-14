# Generated by Django 3.1.2 on 2020-10-08 19:56

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('pilga_project', '0018_auto_20201008_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency_image', to=settings.FILER_IMAGE_MODEL, verbose_name='Изображение'),
        ),
    ]
