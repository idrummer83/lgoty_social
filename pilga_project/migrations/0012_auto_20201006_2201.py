# Generated by Django 3.1.2 on 2020-10-06 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pilga_project', '0011_auto_20201006_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privilege',
            name='document_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='privilege_document_type', to='pilga_project.documenttype', verbose_name='Тип нормативного документа'),
        ),
    ]
