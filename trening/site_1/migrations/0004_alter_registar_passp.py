# Generated by Django 4.2.5 on 2024-03-23 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_1', '0003_alter_registar_passp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registar',
            name='passp',
            field=models.ImageField(blank=True, null=True, upload_to='img-library'),
        ),
    ]
