# Generated by Django 3.1.2 on 2020-10-06 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pilga_project', '0012_auto_20201006_2201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='privilege',
            old_name='type',
            new_name='privilege_type',
        ),
    ]
