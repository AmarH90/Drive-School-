# Generated by Django 4.2.5 on 2024-03-23 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_1', '0002_rename_id_registar_id_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registar',
            name='passp',
            field=models.ImageField(null=True, upload_to='img-library'),
        ),
    ]